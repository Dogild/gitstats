# -*- coding: utf-8 -*-

import datetime
import calendar

from datetime import timedelta, time

from gitstats.lib.github_connection import GithubConnection
from gitstats.lib.task_manager import TaskManager
from gitstats.models.repository import Repository
from gitstats.models.commit import Commit
from gitstats.models.issue import Issue
from gitstats.models.user import User
from gitstats.lib.routes import make_uri_user, make_uri_search_issue, make_uri_orgs
from gitstats.lib.utils import date_utc_to_user_time_zone, set_token

class Account(object):

    def __init__(self, username, timezone, token=None):
        self.user = User(username, timezone)
        self.repositories = list()
        self.forks = list()
        self.orgs = list()
        self.contributions = list()
        self.total_contributions = 0
        self.end_date = datetime.datetime.today()
        self.start_date = self.end_date - datetime.timedelta(days=364)

        set_token(token)

    def get_contributions_of_last_year(self):
        """ Return the contributions of the last year, return an array of 365 arrays """

        return self.get_contributions_of_last_year_from_date(datetime.datetime.today())

    def get_contributions_of_last_three_months(self):
        """ Return the contributions of the last three months, return an array of 91 arrays """

        return self.get_contributions_of_last_three_months_from_date(datetime.datetime.today())

    def get_contributions_of_last_six_months(self):
        """ Return the contributions of the last six months, return an array of 183 arrays """

        return self.get_contributions_of_last_six_months_from_date(datetime.datetime.today())

    def get_contributions_of_last_year_from_date(self, date):
        """ Return the contributions of the last year from the given date, return an array of 183 arrays """

        return self.get_contributions_for_dates(date - datetime.timedelta(days=364), date)

    def get_contributions_of_last_three_months_from_date(self, date):
        """ Return the contributions of the last three months from the given date, return an array of 91 arrays """

        return self.get_contributions_for_dates(date - datetime.timedelta(days=90), date)

    def get_contributions_of_last_six_months_from_date(self, date):
        """ Return the contributions of the last three months from the given date, return an array of 183 arrays """

        return self.get_contributions_for_dates(date - datetime.timedelta(days=182), date)

    def get_contributions_for_dates(self, start_date, end_date):
        """ Return the contributions for the given start_date and end_date, return an array """

        if start_date > end_date:
            return list()

        self.end_date = datetime.datetime.combine(end_date, time.max)
        self.start_date = datetime.datetime.combine(start_date - timedelta(days=1), time.min)

        self.contributions = self._get_contributions()

        return self.contributions

    def sync_user_account(self):
        """ Get the informations for an account, this method will fetch the repos associated to the account (fork and organization repos). """

        task_manager = TaskManager()
        task_manager.launch_request(self._get_users, params=[make_uri_user(self.user.name)])
        task_manager.launch_request(self._get_orgs, params=[make_uri_orgs(self.user.name), dict(), self.orgs])
        task_manager.wait_until_exit()

    def _get_users(self, uri, params=dict()):
        """ Get the repos of the users """

        dict_user = GithubConnection(self.user.name).get(uri, params)

        if "repos_url" in dict_user:
            self.user.repos_url = dict_user["repos_url"]
        else :
            raise AccountNameException("User %s not found" % self.user.name)

    def _get_orgs(self, uri, params=dict(), fetcher=list()):
        """ Get the organizations repos of the users """

        orgs = GithubConnection(self.user.name).get(uri, params)
        fetcher.extend(orgs)

        return orgs

    def _get_contributions(self):
        """ Get the contributions of the user
            This method will firstly fetch the user's informations, then the repositories of the user, then the commits and issues
        """

        self.total_contributions = 0

        number_days = (self.end_date - self.start_date).days

        contributions_list = [list()] * (number_days)
        commits = list()
        issues = list()

        task_manager_issues = TaskManager()
        task_manager_issues.launch_request(self.get_issues, params=[self.start_date, self.end_date, issues])

        self.sync_user_account()
        self.repositories = self.fetch_repositories()

        task_manager = TaskManager()
        task_manager.launch_request(self.get_commits, params=[commits])
        task_manager.wait_until_exit()
        task_manager_issues.wait_until_exit()

        for commit in commits:
            day_number = (self.end_date - commit.date).days
            contributions = [commit]
            contributions.extend(contributions_list[day_number])
            contributions_list[day_number] = contributions
            self.total_contributions += 1

        #print issues

        for issue in issues:
            day_number = (self.end_date - issue.date).days
            contributions = [issue]
            contributions.extend(contributions_list[day_number])
            contributions_list[day_number] = contributions
            self.total_contributions += 1

        return contributions_list[::-1]

    def _get_repositories(self, uri, params=dict(), fetcher=list()):
        """ Fetch repositories with the given URI """

        repositories = GithubConnection(self.user.name).get(uri, params)
        fetcher.extend(repositories)

        return repositories

    def _get_repository(self, uri, params=dict(), destinations=dict()):
        """ Fetch a specific repository with the given URI, this is used when having a fork repository """

        repository = GithubConnection(self.user.name).get(uri, params)

        destinations["commits_url"] = repository["parent"]["commits_url"]
        destinations["url"] = repository["parent"]["url"]
        destinations["issues_url"] = repository["parent"]["issues_url"]

        return repository

    def fetch_repositories(self):
        """ Fetch the repositories of the account, this is going to fetch the root repo (when there are forks) and organization repos"""

        params = dict()
        params["type"] = "all"

        dict_repositories = list()
        task_manager = TaskManager()

        task_manager.launch_request(self._get_repositories, [self.user.repos_url, params, dict_repositories])

        for org in self.orgs:
            task_manager.launch_request(self._get_repositories , [org["repos_url"], dict(), dict_repositories])

        task_manager.wait_until_exit()

        for repository in dict_repositories:
            is_fork = repository["fork"]

            if (is_fork):
                task_manager.launch_request(self._get_repository, [repository["url"], dict(), repository])

        task_manager.wait_until_exit()

        repositories = list()

        for repository in dict_repositories:
            new_repository = Repository(repository["name"], is_fork, self.user.name, repository["commits_url"], repository["url"], repository["issues_url"])

            if new_repository not in repositories:
                repositories.append(new_repository)

        return repositories

    def _get_commits_for_repository(self, uri, params=dict(), fetcher=list()):
        """ Get the commits for the given repo URI"""

        params = dict()
        params["author"] = self.user.name
        params["since"] = self.start_date.isoformat()
        params["until"] = self.end_date.isoformat()

        commits = list()

        new_commits = GithubConnection(self.user.name).get(uri, params)

        for new_commit in new_commits:
            date = datetime.datetime.strptime(new_commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
            date = date_utc_to_user_time_zone(date, self.user.timezone)

            commit = Commit(date=date, sha=new_commit["sha"], author=new_commit["commit"]["author"]["name"], message=new_commit["commit"]["message"])
            commits.append(commit)

        fetcher.extend(commits)

        return commits

    def get_commits(self, fetcher=list()):
        """ Get the commits made by the user for his associated repo"""

        task_manager= TaskManager()
        commits = list()

        for repository in self.repositories:
            task_manager.launch_request(self._get_commits_for_repository, [repository.commits_url, list(), commits])

        task_manager.wait_until_exit()

        fetcher.extend(commits)

        return commits

    def get_issues(self, start_date, end_date, fetcher=list()):
        """ Get the issues opened by the user for the given dates"""

        params = dict()
        params["q"] = "author:%s" % self.user.name

        issues = list()

        dict_issues = GithubConnection(self.user.name).search_issues(uri=make_uri_search_issue(), params=params, min_date=start_date)

        for dict_issue in dict_issues:
            date = datetime.datetime.strptime(dict_issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            date = date_utc_to_user_time_zone(date, self.user.timezone)

            if date > start_date and date < end_date:
                issue = Issue(date=date, author=dict_issue["user"]["login"], number=dict_issue["number"], title=dict_issue["title"])
                issues.append(issue)

        fetcher.extend(issues)

        return issues


class AccountNameException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)