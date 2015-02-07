# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import tornado.web
import tornado.auth

from strava.connection import StravaConnection
from config import Settings


class AuthLoginHandler(tornado.web.RequestHandler, tornado.auth.OAuth2Mixin):

    def get(self):
        settings = Settings()
        connection = StravaConnection()

        if self.get_argument('code', None):
            code = self.get_argument('code')
            self.render("base.html", code=code)
        else:
            redirect_url = "{}{}".format(
                settings.APP_BASE_URL, self.reverse_url('login'))

            auth_url = connection.authentication_url(
                client_id=settings.STRAVA_CLIENT_ID,
                redirect_url=redirect_url,
                approval_prompt=settings.APPROVAL_PROMPT
            )

            self.render("base.html", auth_url=auth_url)