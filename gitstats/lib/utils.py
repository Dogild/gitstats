# -*- coding: utf-8 -*-

import os

from base64 import urlsafe_b64encode

token = os.environ["GITSTATS_TOKEN"]

def make_headers():
    headers = dict()
    headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("%s:x-oauth-basic" % token))
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    return headers