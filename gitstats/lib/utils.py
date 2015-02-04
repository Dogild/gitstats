# -*- coding: utf-8 -*-

import re
import datetime
import os



def date_utc_to_user_time_zone(date, timezone):
    return date - datetime.timedelta(seconds=timezone)

