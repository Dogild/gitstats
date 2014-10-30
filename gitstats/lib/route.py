# -*- coding: utf-8 -*-

github_api = "https://api.github.com/"

def make_uri_user_repository(username):
    return "%susers/%s/repos" % (github_api, username)