# -*- coding: utf-8 -*-

import datetime
import calendar
from datetime import timedelta

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

        task_manager= TaskManager()

        task_manager._launch_request(self._get_users, params=[make_uri_user(self.user.name)])
        task_manager._launch_request(self._get_orgs, params=[make_uri_orgs(self.user.name), dict(), self.orgs])
        task_manager._wait_until_exit()

        self.repositories = self._fetch_repositories()

    def get_contributions_of_last_year(self):
        return self.get_contributions_for_dates(datetime.datetime.today() - datetime.timedelta(days=365), datetime.datetime.today())

    def get_contributions_for_dates(self, start_date, end_date):

        if start_date > end_date:
            return list()

        self.end_date = end_date
        self.start_date = start_date

        return self._get_contributions()

    def _get_users(self, uri, params=dict()):
        dict_user = GithubConnection(self.user.name).get(uri, params)
        self.user.repos_url = dict_user["repos_url"]

    def _get_orgs(self, uri, params=dict(), fetcher=list()):

        orgs = GithubConnection(self.user.name).get(uri, params)
        fetcher.extend(orgs)

        return orgs

    def _get_contributions(self):
        self.total_contributions = 0

        number_days = (self.end_date - self.start_date).days
        contributions_list = [list()] * (number_days + 1)

        commits = list()
        issues = list()

        task_manager= TaskManager()
        task_manager._launch_request(self._get_commits, params=[self.start_date, self.end_date, commits])
        task_manager._launch_request(self._get_issues, params=[self.start_date, self.end_date, issues])

        task_manager._wait_until_exit()

        for commit in commits:
            day_number = (self.end_date + timedelta(days=1) - commit.date).days
            contributions = [commit]
            contributions.extend(contributions_list[day_number])
            contributions_list[day_number] = contributions
            self.total_contributions += 1

        for issue in issues:
            day_number = (self.end_date + timedelta(days=1) - issue.date).days
            contributions = [issue]
            contributions.extend(contributions_list[day_number])
            contributions_list[day_number] = contributions
            self.total_contributions += 1

        return contributions_list[::-1]

    def _get_repositories(self, uri, params=dict(), fetcher=list()):
        repositories = GithubConnection(self.user.name).get(uri, params)
        fetcher.extend(repositories)

        return repositories

    def _get_repository(self, uri, params=dict(), destinations=dict()):
        repository = GithubConnection(self.user.name).get(uri, params)

        destinations["commits_url"] = repository["parent"]["commits_url"]
        destinations["url"] = repository["parent"]["url"]
        destinations["issues_url"] = repository["parent"]["issues_url"]

        return repository

    def _fetch_repositories(self):

        params = dict()
        params["type"] = "all"

        dict_repositories = list()
        task_manager= TaskManager()

        task_manager._launch_request(self._get_repositories, [self.user.repos_url, params, dict_repositories])

        for org in self.orgs:
            task_manager._launch_request(self._get_repositories , [org["repos_url"], dict(), dict_repositories])

        task_manager._wait_until_exit()

        for repository in dict_repositories:
            is_fork = repository["fork"]

            if (is_fork):
                task_manager._launch_request(self._get_repository, [repository["url"], dict(), repository])

        task_manager._wait_until_exit()

        repositories = list()

        for repository in dict_repositories:
            new_repository = Repository(repository["name"], is_fork, self.user.name, repository["commits_url"], repository["url"], repository["issues_url"])

            if new_repository not in repositories:
                repositories.append(new_repository)

        return repositories

    def _get_commits_for_repository(self, uri, params=dict(), fetcher=list()):

        params = dict()
        params["author"] = self.user.name
        params["since"] = self.start_date.isoformat()
        params["until"] = self.end_date.isoformat()

        commits = list()

        new_commits = GithubConnection(self.user.name).get(uri, params)

        for new_commit in new_commits:
            date = datetime.datetime.strptime(new_commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
            commit = Commit(date=date, sha=new_commit["sha"], author=new_commit["commit"]["author"]["name"], message=new_commit["commit"]["message"])
            commits.append(commit)

        fetcher.extend(commits)

        return commits

    def _get_commits(self, start_date, end_date, fetcher=list()):

        task_manager= TaskManager()
        commits = list()

        for repository in self.repositories:
            task_manager._launch_request(self._get_commits_for_repository, [repository.commits_url, list(), commits])

        task_manager._wait_until_exit()

        fetcher.extend(commits)

        return commits

    def _get_issues(self, start_date, end_date, fetcher=list()):

        params = dict()
        params["q"] = "author:%s" % self.user.name

        issues = list()

        dict_issues = GithubConnection(self.user.name).search_issues(uri=make_uri_search_issue(), params=params, min_date=start_date)

        for dict_issue in dict_issues:
            date = datetime.datetime.strptime(dict_issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            issue = Issue(date=date, author=dict_issue["user"]["login"], number=dict_issue["number"], title=dict_issue["title"])

            if date > start_date:
                issues.append(issue)

        fetcher.extend(issues)

        return issues