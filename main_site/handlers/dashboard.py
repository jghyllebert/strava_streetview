# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import json

import requests
from tornado.web import RequestHandler

from settings import STRAVA_BASE_URL


class BaseLoginHandler(RequestHandler):
    """
    Check if User is logged in
    """
    def get(self, *args, **kwargs):
        if not self.get_secure_cookie('auth_user'):
            self.redirect(self.reverse_url('landing'))
        self.user = json.loads(self.get_secure_cookie('auth_user'))

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)


class DashboardHandler(BaseLoginHandler):

    def get(self, *args, **kwargs):
        super(DashboardHandler, self).get(*args, **kwargs)

        # Statistics
        koms_url = "{}api/v3/athletes/{}/koms?access_token={}".format(
            STRAVA_BASE_URL,
            self.user['athlete']['id'],
            self.user['access_token']
        )
        statistics_url = "{}api/v3/athletes/{}/stats?access_token={}".format(
            STRAVA_BASE_URL,
            self.user['athlete']['id'],
            self.user['access_token']
        )

        koms = requests.get(koms_url)
        statistics = requests.get(statistics_url)

        # Activities
        activities_url = "{}api/v3/athlete/activities?access_token={}".format(
            STRAVA_BASE_URL, self.user['access_token'])
        activities = requests.get(activities_url)

        return self.render(
            "dashboard.html",
            user=self.user['athlete'],
            achievements=json.loads(statistics.text),
            koms=json.loads(koms.text),
            activities=json.loads(activities.text),
        )