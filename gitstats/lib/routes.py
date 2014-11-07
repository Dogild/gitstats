# -*- coding: utf-8 -*-

github_api = "https://api.github.com/"

def make_uri_user(username):
    return "%susers/%s" % (github_api, username)

def make_uri_search_issue():
    return "%ssearch/issues" % (github_api)

def make_uri_orgs(username):
    return "%susers/%s/orgs" % (github_api, username)