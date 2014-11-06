# -*- coding: utf-8 -*-

import json
import requests

from gitstats.lib.utils import make_headers, transform_url
from gitstats.models.repository import Repository

class GithubConnection(object):

    def __init__(self, username):
        self.username = username

    def get(self, uri, params=dict(), transform_uri=True):

        if (transform_uri):
            uri = "%s?" % transform_url(uri)
            uri_params = ""

            for param in params:
                if len(uri_params):
                    uri_params = "%s&%s=%s" % (uri_params, param, params[param])
                else:
                    uri_params = "%s=%s" % (param, params[param])

            uri = uri + uri_params

        try:
            r = requests.get(uri, headers=make_headers())
        except Exception as exc:
            raise Exception("Requests issue %s" % exc)

        next_pages = list()

        if "next" in r.links:
            next_pages = self.get(r.links["next"]["url"], transform_uri=False)

        if r.status_code >= 300 :
            print "HTTP Error %s \n%s : %s" % (uri, r.status_code, r.json())
            return dict()

        result_json = r.json()

        if isinstance(result_json ,list) and len(next_pages):
            result_json.extend(next_pages)

        return result_json