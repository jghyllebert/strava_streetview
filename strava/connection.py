# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import urllib

from config import settings


class StravaConnection(object):

    default_authentication_fields = {'response_type': 'code'}

    def __init__(self, client_id):
        self.client_id = client_id

    def authentication_url(self, redirect_url, **kwargs):
        """
        Build the authentication url to login with the Strava API.
        """
        return "{}oauth/authorize{}&client_id={}&redirect_uri={}{}".format(
            settings.STRAVA_BASE_URL,
            self._add_fields(self.default_authentication_fields, '?'),
            self.client_id,
            redirect_url,
            self._add_fields(kwargs, '&')
        )

    def _add_fields(self, fields, prefix=None):
        url = "{}".format(prefix) if prefix else ""
        for key, value in fields.iteritems():
            url += "{}={}&".format(key, self._encode(value))
        return url[:-1]  # remove last question mark

    def _encode(self, word):
        if isinstance(word, unicode):
            return urllib.quote_plus(word.encode("utf-8"))
        return word.lower()

    def exchange_token_url(
            self, token, client_secret=settings.STRAVA_CLIENT_SECRET):
        """
        Build the exchange token to get data back from Strava.
        """
        return "{}oauth/token?client_id={}&code={}&client_secret={}".format(
            settings.STRAVA_BASE_URL,
            self.client_id,
            token,
            client_secret
        )