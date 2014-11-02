# -*- coding: utf-8 -*-

class Repository(object):

    def __init__(self, name, fork, owner, commits_url, repo_url):
        self.name = name
        self.fork = fork
        self.owner = owner
        self.commits_url = commits_url
        self.repos_url = repo_url
        self.commits = list()

    def __repr__(self):
        return "\nRepository : %s" % self.name

    def __str__(self):
        return "\nRepository : %s" % self.name