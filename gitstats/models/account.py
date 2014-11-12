# -*- coding: utf-8 -*-

import datetime
import calendar

from gitstats.lib.github_connection import GithubConnection
from gitstats.lib.task_manager import TaskManager
from gitstats.models.repository import Repository
from gitstats.models.commit import Commit
from gitstats.models.issue import Issue
from gitstats.models.user import User
from gitstats.lib.routes import make_uri_user, make_uri_search_issue, make_uri_orgs

class Account(object):

    def __init__(self, username):
        self.user = User(username)
        self.repositories = list()
        self.forks = list()
        self.orgs = list()
        self.total_contributions = 0
        self.end_date = datetime.datetime.today()
        self.start_date = self.end_date - datetime.timedelta(days=365)
        self.github_connection = GithubConnection(username)
        self.task_manager= TaskManager()

        self.task_manager._launch_request(make_uri_user(self.user.name), self._get_users)
        self.task_manager._launch_request(make_uri_orgs(self.user.name), self._get_orgs, destinations=self.orgs)
        self.task_manager._wait_until_exit()

        self.repositories = self._fetch_repositories()

    def get_contributions_of_last_year(self):
        return self.get_contributions_for_dates(datetime.datetime.today() - datetime.timedelta(days=365), datetime.datetime.today())

    def get_contributions_for_dates(self, start_date, end_date):

        if start_date > end_date:
            return list()

        self.end_date = end_date
        self.start_date = start_date

        return self._get_contributions()

    def _get_users(self, uri, params=list(), destinations=dict()):
        dict_user = self.github_connection.get(uri)
        self.user.repos_url = dict_user["repos_url"]

    def _get_orgs(self, uri, params=list(), destinations=list()):
        destinations.extend(self.github_connection.get(uri))

    def _get_contributions(self):
        self.total_contributions = 0
        contributions_list = [list()] * (self.end_date - self.start_date).days

        commits = self._get_commits(self.start_date, self.end_date)
        issues = self._get_issues(self.start_date, self.end_date)

        for commit in commits:
            day_number = commit.date.timetuple().tm_yday
            contributions = [commit]
            contributions.extend(contributions_list[day_number])
            contributions_list[day_number] = contributions
            self.total_contributions += 1

        for issue in issues:
            day_number = issue.date.timetuple().tm_yday
            contributions = [issue]
            contributions.extend(contributions_list[day_number])
            contributions_list[day_number] = contributions
            self.total_contributions += 1

        return contributions_list

    def _get_repositories(self, uri, params=list(), destinations=list()):
        destinations.extend(self.github_connection.get(uri, params))

    def _get_repository(self, uri, params=list(), destinations=dict()):
        repository = (self.github_connection.get(uri, params))

        destinations["commits_url"] = repository["parent"]["commits_url"]
        destinations["url"] = repository["parent"]["url"]
        destinations["issues_url"] = repository["parent"]["issues_url"]

    def _fetch_repositories(self):

        params = dict()
        params["type"] = "all"

        dict_repositories = list()

        self.task_manager._launch_request(self.user.repos_url, self._get_repositories, params, dict_repositories)

        for org in self.orgs:
            self.task_manager._launch_request(org["repos_url"], self._get_repositories, destinations=dict_repositories)

        self.task_manager._wait_until_exit()


        for repository in dict_repositories:
            is_fork = repository["fork"]

            if (is_fork):
                self.task_manager._launch_request(repository["url"], self._get_repository, destinations=repository)

        self.task_manager._wait_until_exit()


        repositories = list()

        for repository in dict_repositories:
            new_repository = Repository(repository["name"], is_fork, self.user.name, repository["commits_url"], repository["url"], repository["issues_url"])

            if new_repository not in repositories:
                repositories.append(new_repository)

        return repositories

    def _get_commits_for_repository(self, repository, start_date, end_date):

        params = dict()
        params["author"] = self.user.name
        params["since"] = start_date.isoformat()
        params["until"] = end_date.isoformat()

        commits = list()

        new_commits = self.github_connection.get(repository.commits_url, params)

        for new_commit in new_commits:
            date = datetime.datetime.strptime(new_commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
            commit = Commit(date=date, sha=new_commit["sha"], author=new_commit["commit"]["author"]["name"], message=new_commit["commit"]["message"])
            commits.append(commit)

        return commits

    def _get_commits(self, start_date, end_date, destinations=list()):

        commits = list()

        for repository in self.repositories:
            commits.extend(self._get_commits_for_repository(repository, start_date, end_date))

        destinations.extend(commits)

        return commits

    def _get_issues(self, start_date, end_date):

        params = dict()
        params["q"] = "author:%s" % self.user.name

        issues = list()

        dict_issues = self.github_connection.search_issues(uri=make_uri_search_issue(), params=params, min_date=start_date)

        for dict_issue in dict_issues:
            date = datetime.datetime.strptime(dict_issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            issue = Issue(date=date, author=dict_issue["user"]["login"], number=dict_issue["number"], title=dict_issue["title"])

            if date > start_date:
                issues.append(issue)

        return issues