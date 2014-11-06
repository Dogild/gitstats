# -*- coding: utf-8 -*-

class Repository(object):

    def __init__(self, name, fork, owner, commits_url, repos_url):
        self.name = name
        self.fork = fork
        self.owner = owner
        self.commits_url = commits_url
        self.repos_url = repos_url
        self.commits = list()

    def __repr__(self):
        return "\nRepository : %s" % self.repos_url

    def __str__(self):
        return "\nRepository : %s" % self.repos_url

    def __eq__(self, other):
        return self.repos_url == other.repos_url