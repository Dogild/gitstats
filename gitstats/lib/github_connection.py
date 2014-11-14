# -*- coding: utf-8 -*-

import json
import requests
import datetime

from gitstats.lib.utils import make_headers, transform_url
from gitstats.models.repository import Repository

class GithubConnection(object):

    def __init__(self, username):
        self.username = username

    def _invoke_request(self, uri):

        print uri

        try:
            r = requests.get(uri, headers=make_headers())
        except Exception as exc:
            raise Exception("Requests issue %s" % exc)

        if r.status_code >= 300 :
            raise Exception("HTTP Error %s \n%s : %s" % (uri, r.status_code, r.json()))

        return r

    def _add_params(self, uri, params):

        uri = "%s?" % transform_url(uri)
        uri_params = ""

        params["per_page"] = 100

        for param in params:
            if len(uri_params):
                uri_params = "%s&%s=%s" % (uri_params, param, params[param])
            else:
                uri_params = "%s=%s" % (param, params[param])

        uri = uri + uri_params

        return uri

    def get(self, uri, params=dict(), transform_uri=True):

        if (transform_uri):
            uri = self._add_params(uri, params)

        try:
            r = self._invoke_request(uri)
        except Exception as exc:
            print "Exception caught %s" % (exc.message)
            return dict()

        result_json = r.json()
        next_pages = list()

        if "next" in r.links:
            next_pages = self.get(r.links["next"]["url"], transform_uri=False)

        if isinstance(result_json ,list) and len(next_pages):
            result_json.extend(next_pages)

        return result_json

    def search_issues(self, uri, params=dict(), transform_uri=True, min_date=None):

        if (transform_uri):
            uri = self._add_params(uri, params)

        try:
            r = self._invoke_request(uri)
        except Exception as exc:
            print "Exception caught %s" % (exc.message)
            return dict()

        result_json = r.json()["items"]
        next_pages = list()

        last_date = datetime.datetime.strptime(result_json[-1]["created_at"], "%Y-%m-%dT%H:%M:%SZ")

        if "next" in r.links and last_date > min_date:
            next_pages = self.search_issues(r.links["next"]["url"], transform_uri=False, min_date=min_date)

        if isinstance(result_json ,list) and len(next_pages):
            result_json.extend(next_pages)

        return result_json