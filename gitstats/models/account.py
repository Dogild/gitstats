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

            is_fork = repository["fork"]
            commits_url = repository["commits_url"]
            repos_url = repository["url"]

            if (is_fork):
                dict_parent = self.github_connection.get(repos_url)
                commits_url = dict_parent["parent"]["commits_url"]
                repos_url = dict_parent["parent"]["url"]

            new_repository = Repository(repository["name"], is_fork, self.username, commits_url, repos_url)

            if new_repository not in repositories:
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
                date = datetime.datetime.strptime(new_commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
                commit = Commit(date=date, sha=new_commit["sha"], author=new_commit["commit"]["author"]["name"], message=new_commit["commit"]["message"])
                commits.append(commit)

        self.contributions += len(commits)

        return commits