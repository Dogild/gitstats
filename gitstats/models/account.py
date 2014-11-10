# -*- coding: utf-8 -*-

import datetime

from gitstats.lib.github_connection import GithubConnection
from gitstats.models.repository import Repository
from gitstats.models.commit import Commit
from gitstats.models.issue import Issue
from gitstats.lib.routes import make_uri_user, make_uri_search_issue, make_uri_orgs

class Account(object):

    def __init__(self, username):
        self.username = username
        self.repositories = list()
        self.forks = list()
        self.contributions = 0
        self.end_date = datetime.datetime.today()
        self.start_date = self.end_date - datetime.timedelta(days=365)
        self.github_connection = GithubConnection(username)

        dict_user = self.github_connection.get(make_uri_user(username))
        self.repos_url = dict_user["repos_url"]
        self.orgs = self.github_connection.get(make_uri_orgs(username))
        self.repositories = self._get_repositories()

    def get_contributions_of_last_year(self):
        self.end_date = datetime.datetime.today()
        self.start_date = self.end_date - datetime.timedelta(days=365)

        return self._get_contributions()

    def get_contributions_for_dates(self, start_date, end_date):
        self.end_date = end_date
        self.start_date = start_date

        return self._get_contributions()

    def _get_contributions(self):
        self.contributions = 0
        contributions_list = list()
        commits = self._get_commits(self.start_date, self.end_date)
        issues = self._get_issues(self.start_date, self.end_date)

        contributions_list.extend(commits)
        contributions_list.extend(issues)

        return contributions_list

    def _get_repositories(self):

        params = dict()
        params["type"] = "all"
        dict_repositories = self.github_connection.get(self.repos_url, params)

        for org in self.orgs:
            dict_repositories.extend(self.github_connection.get(org["repos_url"]))

        repositories = list()

        for repository in dict_repositories:
            is_fork = repository["fork"]
            commits_url = repository["commits_url"]
            repos_url = repository["url"]
            issues_url = repository["issues_url"]

            if (is_fork):
                dict_parent = self.github_connection.get(repos_url)
                commits_url = dict_parent["parent"]["commits_url"]
                repos_url = dict_parent["parent"]["url"]
                issues_url = dict_parent["parent"]["issues_url"]

            new_repository = Repository(repository["name"], is_fork, self.username, commits_url, repos_url, issues_url)

            if new_repository not in repositories:
                repositories.append(new_repository)

        return repositories

    def _get_commits_for_repository(self, repository, start_date, end_date):

        params = dict()
        params["author"] = self.username
        params["since"] = start_date.isoformat()
        params["until"] = end_date.isoformat()

        commits = list()

        new_commits = self.github_connection.get(repository.commits_url, params)

        for new_commit in new_commits:
            date = datetime.datetime.strptime(new_commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
            commit = Commit(date=date, sha=new_commit["sha"], author=new_commit["commit"]["author"]["name"], message=new_commit["commit"]["message"])
            commits.append(commit)

        return commits

    def _get_commits(self, start_date, end_date):

        commits = list()

        for repository in self.repositories:
            commits.extend(self._get_commits_for_repository(repository, start_date, end_date))

        return commits

    def _get_issues(self, start_date, end_date):

        params = dict()
        params["q"] = "author:%s" % self.username

        issues = list()

        dict_issues = self.github_connection.search_issues(uri=make_uri_search_issue(), params=params, min_date=start_date)

        for dict_issue in dict_issues:
            date = datetime.datetime.strptime(dict_issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            issue = Issue(date=date, author=dict_issue["user"]["login"], number=dict_issue["number"], title=dict_issue["title"])

            if date > start_date:
                issues.append(issue)

        return issues