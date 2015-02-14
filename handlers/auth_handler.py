# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import json

import tornado.web
import tornado.auth
import requests

from strava.connection import StravaConnection
from config import Settings


class AuthLoginHandler(tornado.web.RequestHandler):

    def get(self):
        settings = Settings()
        connection = StravaConnection(settings.STRAVA_CLIENT_ID)

        redirect_url = "{}{}".format(
            settings.APP_BASE_URL, self.reverse_url('exchange'))

        auth_url = connection.authentication_url(
            redirect_url=redirect_url,
            approval_prompt=settings.APPROVAL_PROMPT
        )

        error = self.get_argument("error", None)

        self.render("base.html", auth_url=auth_url, error=error)


class ExchangeHandler(tornado.web.RequestHandler, tornado.auth.OAuth2Mixin):

    def get(self, *args, **kwargs):
        if self.get_argument('error', None):
            error = self.get_argument('error')
            self.redirect(
                "{}?error={}".format(self.reverse_url('login'), error))
        else:
            settings = Settings()
            connection = StravaConnection(settings.STRAVA_CLIENT_ID)
            exchange = connection.exchange_token_url(
                self.get_argument('code'), settings.STRAVA_CLIENT_SECRET)

            response = requests.post(exchange)
            data = json.loads(response.text)
            activities = requests.get(
                "https://www.strava.com/api/v3/athlete/activities"
                "?access_token={}".format(data['access_token']))

            self.render(
                "profile.html",
                data=data,
                activities=json.loads(activities.text)
            )