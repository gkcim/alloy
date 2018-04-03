# -*- coding: utf-8 -*-

from .consts import (
    APP_NAME,
    APP_URI,
)


class Environment(object):

    def __init__(self):
        self._configs = None

    @property
    def app_name(self):
        return APP_NAME

    @property
    def app_uri(self):
        return APP_URI


env = Environment()
