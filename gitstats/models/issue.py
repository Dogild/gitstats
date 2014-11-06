# -*- coding: utf-8 -*-

import datetime

class Issue(object):

    def __init__(self, date=None, number=None, author=None, title=None):
        self.date = date
        self.number = number
        self.author = author
        self.title = title

    def __repr__(self):
        return "\nIssue : %s %s" % (self.author ,self.title)

    def __str__(self):
        return "\nIssue : %s %s" % (self.author ,self.title)