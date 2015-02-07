# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import os

DEBUG = False

STRAVA_BASE_URL = "https://www.strava.com/"
APP_BASE_URL = "http://strava.ghyllebert.be"
APP_PORT_NUMBER = 8000

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
STATIC_PATH = os.path.join(BASE_DIR, 'static')

STRAVA_CLIENT_ID = os.environ.get('STRAVA_CLIENT_ID', None)
STRAVA_CLIENT_SECRET = os.environ.get('STRAVA_CLIENT_SECRET', None)
STRAVA_ACCESS_TOKEN = os.environ.get('STRAVA_ACCESS_TOKEN', None)

APPROVAL_PROMPT = 'auto'