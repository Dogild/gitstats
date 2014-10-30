# -*- coding: utf-8 -*-

import datetime

from gitstats.lib.github_connection import GithubConnection
from gitstats.model.repository import Repository

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

    def get_repositories(self):
        self.repositories = self.github_connection.get_user_repositories()
        return self.repositories