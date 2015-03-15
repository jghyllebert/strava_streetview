# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import tornado.ioloop
import tornado.web
import tornado.httpserver

from settings import (
    TEMPLATE_PATH, STATIC_PATH, DEBUG, COOKIE_SECRET, STRAVA_CLIENT_ID,
    STRAVA_CLIENT_SECRET, STRAVA_ACCESS_TOKEN, APP_PORT_NUMBER
)
from main_site.handlers.main import (
    LoginHandler, LogoutHandler, LandingHandler)
from main_site.handlers.dashboard import DashboardHandler

if __name__ == '__main__':

    app_settings = {
        'template_path': TEMPLATE_PATH,
        'static_path': STATIC_PATH,
        'debug': DEBUG,
        'cookie_secret': COOKIE_SECRET,
        'xsrf_cookies': True,
        'client_id': STRAVA_CLIENT_ID,
        'client_secret': STRAVA_CLIENT_SECRET,
        'access_token': STRAVA_ACCESS_TOKEN,
    }

    application = tornado.web.Application([
        (r"/static/(.*)", tornado.web.StaticFileHandler),
        (r"/dashboard", DashboardHandler, None, "dashboard"),
        (r"/auth/login", LoginHandler, None, "login"),
        (r"/auth/logout", LogoutHandler, None, "logout"),
        (r"/", LandingHandler, None, "landing")
    ], **app_settings)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(APP_PORT_NUMBER)

    tornado.ioloop.IOLoop.instance().start()