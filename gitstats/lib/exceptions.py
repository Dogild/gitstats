# -*- coding: utf-8 -*-


class TokenException(Exception):

    def __str__(self):
        return "Token not defined. Please defined in the the environment var GITSTATS_TOKEN or give it to the constructor of account"
