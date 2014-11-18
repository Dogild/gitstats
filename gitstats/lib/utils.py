# -*- coding: utf-8 -*-

import os
import re

from base64 import urlsafe_b64encode

token = os.environ["GITSTATS_TOKEN"]

def make_headers():
    headers = dict()
    headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("%s:x-oauth-basic" % token))
    #headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("login:pwd"))
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    return headers

def transform_url(url):
    m = re.search('([\w\:\/\.\-]*)', url)
    return m.group(0)
