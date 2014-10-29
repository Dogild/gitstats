# -*- coding: utf-8 -*-

import json
import requests

from gitstats.lib.route import make_uri_user_repository

class GithubConnection(object):

    def __init__(self, username):
        self.username = username

    def get_user_repositories(self):

        r = requests.get(make_uri_user_repository(self.username))
        return r.json()
