# -*- coding: utf-8 -*-

import datetime

class Commit(object):

    def __init__(self, date=None, sha=None, author=None, message=None):
        self.date = date
        self.sha = sha
        self.author = author
        self.message = message

    def __repr__(self):
        return "\nCommit : %s %s" % (self.author ,self.message)

    def __str__(self):
        return "\nCommit : %s %s" % (self.author ,self.message)