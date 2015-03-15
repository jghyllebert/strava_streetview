# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import json
import requests
from tornado.auth import OAuth2Mixin
from tornado.web import RequestHandler
import tornado.gen

from settings import STRAVA_BASE_URL, APP_BASE_URL


class StravaOAuth2Mixin(OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "{}oauth/authorize".format(STRAVA_BASE_URL)
    _OAUTH_ACCESS_TOKEN_URL = "{}oauth/token".format(STRAVA_BASE_URL)

    def get_authenticated_user(self, client_id, client_secret, code):
        user = requests.post("{}?client_id={}&client_secret={}&code={}".format(
            StravaOAuth2Mixin._OAUTH_ACCESS_TOKEN_URL,
            client_id,
            client_secret,
            code
            )
        )

        return user.text


class LoginHandler(RequestHandler, StravaOAuth2Mixin):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        if self.get_secure_cookie('auth_user'):
            self.redirect(self.reverse_url('dashboard'))

        if self.get_argument('code', False):
            user = self.get_authenticated_user(
                client_id=self.settings['client_id'],
                client_secret=self.settings['client_secret'],
                code=self.get_argument('code')
            )

            self.set_secure_cookie('auth_user', user)
            self.redirect(self.reverse_url('dashboard'))
        else:
            yield self.authorize_redirect(
                redirect_uri="{}{}".format(
                    APP_BASE_URL, self.reverse_url('login')),
                client_id=self.settings['client_id'],
                extra_params={'response_type': 'code'}
            )


class LogoutHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.clear_cookie('auth_user')
        self.redirect(self.reverse_url('landing'))


class LandingHandler(RequestHandler):

    def get(self, *args, **kwargs):
        return self.render("landing.html")
