# -*- coding: utf-8 -*-

import datetime

from gitstats.lib.github_connection import GithubConnection
from gitstats.models.repository import Repository
from gitstats.models.commit import Commit
from gitstats.lib.routes import make_uri_user

class Account(object):

    def __init__(self, username, repositories=list(), forks=list(), contributions=0, end_date=datetime.date.today()):
        self.username = username
        self.repositories = repositories
        self.forks = forks
        self.contributions = contributions
        self.end_date = end_date
        self.start_date = end_date - datetime.timedelta(days=365)
        self.github_connection = GithubConnection(username)

        dict_user = self.github_connection.get(make_uri_user(username))
        self.repos_url = dict_user["repos_url"]

    def get_repositories(self):

        params = dict()
        params["type"] = "all"
        dict_repositories = self.github_connection.get(self.repos_url, params)

        repositories = list()

        for repository in dict_repositories:
            new_repository = Repository(repository["name"], repository["fork"], self.username, repository["commits_url"], repository["url"])
            repositories.append(new_repository)

        self.repositories = repositories

        return self.repositories

    def get_commits(self):

        params = dict()
        params["author"] = self.username
        params["since"] = self.start_date.isoformat()
        params["until"] = self.end_date.isoformat()

        commits = list()

        for repository in self.repositories:
            new_commits = self.github_connection.get(repository.commits_url, params)

            for new_commit in new_commits:
                commit = Commit(date=new_commit["commit"]["author"]["date"], sha=new_commit["sha"], author=new_commit["commit"]["author"]["name"], message=new_commit["commit"]["message"])
                commits.append(commit)

        self.contributions += len(commits)

        return commits