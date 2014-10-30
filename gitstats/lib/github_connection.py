# -*- coding: utf-8 -*-

import json
import requests

from gitstats.lib.route import make_uri_user_repository
from gitstats.lib.utils import make_headers
from gitstats.models.repository import Repository

class GithubConnection(object):

    def __init__(self, username):
        self.username = username

    def get_user_repositories(self):

        try:
            r = requests.get(make_uri_user_repository(self.username), headers=make_headers())
        except Exception as exc:
            print "Unexpected error:", exc
            raise Exception("requests issue")

        dict_repositories = r.json()

        if not isinstance(dict_repositories, list):
            print "We should get a list when getting the repositories, but we got %s", dict_repositories
            raise Exception("List issue")

        repositories = list()

        for repository in dict_repositories:
            new_repository = Repository(repository["name"], repository["fork"], self.username, repository["commits_url"], repository["url"])
            repositories.append(new_repository)

        return repositories

