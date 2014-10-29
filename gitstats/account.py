# -*- coding: utf-8 -*-

import datetime

class Account(object):

    def __init__(self, username, commits=list(), repositories=list(), forks=list(), contributions=0, end_date=datetime.date.today()):
        self.username = username
        self.commits = commits
        self.repositories = repositories
        self.forks = forks
        self.contributions = contributions
        self.end_date = end_date
        self.start_date = end_date - datetime.timedelta(days=365)

    def get_forks():
        pass

    def sort_contributed_forks(forks):
        pass

    def get_repositories():
        pass

    def get_commits_for_repositeries(repository):
        pass

    def get_commits_for_fork(fork):
        pass