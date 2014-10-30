# -*- coding: utf-8 -*-

import json
import requests

from gitstats.lib.utils import make_headers
from gitstats.models.repository import Repository

class GithubConnection(object):

    def __init__(self, username):
        self.username = username

    def invoke(self, uri):
        try:
            r = requests.get(uri, headers=make_headers())
        except Exception as exc:
            raise Exception("Requests issue %s" % exc)

        if r.status_code >= 300 :
            raise Exception("HTTP Error %s : %s" % (r.status_code, r.json()))

        return r.json()