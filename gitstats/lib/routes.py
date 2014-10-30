# -*- coding: utf-8 -*-

github_api = "https://api.github.com/"

def make_uri_user(username):
    return "%susers/%s" % (github_api, username)