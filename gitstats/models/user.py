# -*- coding: utf-8 -*-

class User(object):

    def __init__(self, name, timezone, repos_url=None):
        self.name = name
        self.repos_url = repos_url
        self.timezone = timezone

    def __repr__(self):
        return "\nUser : %s" % self.name

    def __str__(self):
        return "\nUser : %s" % self.name

    def __eq__(self, other):
        return self.name == other.name