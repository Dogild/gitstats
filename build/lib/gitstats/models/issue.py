# -*- coding: utf-8 -*-

import datetime

class Issue(object):

    def __init__(self, date=None, number=None, author=None, title=None):
        self.date = date
        self.number = number
        self.author = author
        self.title = title

    def __repr__(self):
        return "\nIssue %s : %s %s" % (self.date, self.author.encode('utf-8') ,self.title.encode('utf-8'))

    def __str__(self):
        return "\nIssue %s : %s %s" % (self.date, self.author.encode('utf-8') ,self.title.encode('utf-8'))