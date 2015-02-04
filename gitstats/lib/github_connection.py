# -*- coding: utf-8 -*-


import datetime
import os
import re
import requests

from base64 import urlsafe_b64encode

from gitstats.lib.exceptions import TokenException

class GithubConnection(object):

    def __init__(self, username, token=None):
        self.username = username
        self.token = token

    def _get_headers(self):
        """ Get headers for the given connection
        """

        oauth_token = self.token
        if oauth_token is None:
            if  "GITSTATS_TOKEN" in os.environ:
                oauth_token = os.environ["GITSTATS_TOKEN"]
            else:
                raise TokenException("Unknown token")

        headers = dict()
        headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("%s:x-oauth-basic" % oauth_token))
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        return headers

    def _transform_url(self, url):
        """ This method will return the URL after having removed the extra informations of the URL got by github.
            For instance, /commits/{sha} the string {sha} will be removed
        """

        m = re.search('([\w\:\/\.\-]*)', url)
        uri = m.group(0)

        if uri[-1:] == "/":
            uri = uri[:-1]

        return uri


    def _invoke_request(self, uri):
        """ Launch a request with requests
            This method a Exception when the HTTP error is over or equal to 300
        """

        try:
            r = requests.get(uri, headers=self._get_headers())
        except Exception as exc:
            raise Exception("Requests issue %s" % exc)

        if r.status_code >= 300 :
            raise Exception("HTTP Error %s \n%s : %s" % (uri, r.status_code, r.json()))

        return r

    def _add_params(self, uri, params):
        """ Add the given params to the given URI """

        uri = "%s?" % self._transform_url(uri)
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
        """ Make a get call on the given URI
            This method will continue to make new requests with the URI of the header next. It automatically fetch informations of the next pages
            The param transform_uri allows you to remove or not the extra informations given by github for their given URI.
        """

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
        """ Make a get call on the given URI
            This method will continue to make new requests with the URI of the header next. It automatically fetch informations of the github pagination
            The param transform_uri allows you to remove or not the extra informations given by github for their given URI.
            The param min_date is used to know when we need to stop to fetch informations of the next pages
        """

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