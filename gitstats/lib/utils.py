# -*- coding: utf-8 -*-

import re
import datetime

from base64 import urlsafe_b64encode

oath_token = None

def make_headers():
    """ Return a dictionary with the needed headers for github
        The dictionary will have the keys Authorization, Content-Type and Accept
    """

    headers = dict()
    headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("%s:x-oauth-basic" % oath_token))
    #headers["Authorization"] = "Basic %s" % (urlsafe_b64encode("login:password"))
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    return headers

def transform_url(url):
    """ This method will return the URL after having removed the extra informations of the URL got by github.
        For instance, /commits/{sha} the string {sha} will be removed
    """

    m = re.search('([\w\:\/\.\-]*)', url)
    uri = m.group(0)

    if uri[-1:] == "/":
        uri = uri[:-1]

    return uri

def date_utc_to_user_time_zone(date, timezone):
    return date - datetime.timedelta(seconds=timezone)
