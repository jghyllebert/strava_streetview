# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import os

DEBUG = bool(os.environ.get('DEBUG', False))
APPROVAL_PROMPT = os.environ.get('STRAVA_APPROVAL_PROMPT', 'auto')
STRAVA_BASE_URL = "https://www.strava.com/"
APP_BASE_URL = os.environ.get('APP_BASE_URL', "http://strava.ghyllebert.be")
APP_PORT_NUMBER = 8000

if DEBUG:
    APP_BASE_URL += ":{}".format(APP_PORT_NUMBER)

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
STATIC_PATH = os.path.join(BASE_DIR, 'static')

STRAVA_CLIENT_ID = os.environ['STRAVA_CLIENT_ID']
STRAVA_CLIENT_SECRET = os.environ['STRAVA_CLIENT_SECRET']
STRAVA_ACCESS_TOKEN = os.environ['STRAVA_ACCESS_TOKEN']

COOKIE_SECRET = os.environ['COOKIE_SECRET']