# -*- coding: utf-8 -*-

import os
import re

from base64 import urlsafe_b64encode

token = os.environ["GITSTATS_TOKEN"]

def make_headers():
    """ Return a dictionary with the needed headers for github
        The dictionary will have the keys Authorization, Content-Type and Accept
    """

    headers = dict()
    headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("%s:x-oauth-basic" % token))
    #headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("login:password"))
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    return headers

def transform_url(url):
    """ This method will return the URL after having removed the extra informations of the URL got by github.
        For instance, /commits/{sha} the string {sha} will be removed
    """

    m = re.search('([\w\:\/\.\-]*)', url)
    return m.group(0)
