# -*- coding: utf-8 -*-

import datetime

class Commit(object):

    def __init__(self, date=None, ID=None, author=None, comment=None):
        self.date = date
        self.ID = ID
        self.author = author
        self.comment = comment