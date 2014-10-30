# -*- coding: utf-8 -*-

import datetime

from gitstats.lib.github_connection import GithubConnection
from gitstats.models.repository import Repository
from gitstats.lib.routes import make_uri_user

class Account(object):

    def __init__(self, username, commits=list(), repositories=list(), forks=list(), contributions=0, end_date=datetime.date.today()):
        self.username = username
        self.commits = commits
        self.repositories = repositories
        self.forks = forks
        self.contributions = contributions
        self.end_date = end_date
        self.start_date = end_date - datetime.timedelta(days=365)
        self.github_connection = GithubConnection(username)

        dict_user = self.github_connection.invoke(make_uri_user(username))
        self.repos_url = dict_user["repos_url"]

    def get_repositories(self):

        dict_repositories = self.github_connection.invoke(self.repos_url)

        repositories = list()

        for repository in dict_repositories:
            new_repository = Repository(repository["name"], repository["fork"], self.username, repository["commits_url"], repository["url"])
            repositories.append(new_repository)

        self.repositories = repositories

        return self.repositories