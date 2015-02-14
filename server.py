# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import argparse
import os

import tornado.ioloop
import tornado.web
import tornado.httpserver

from handlers.auth_handler import AuthLoginHandler, ExchangeHandler
from config import set_environ, Settings

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="start the tornado server")
    parser.add_argument('--settings')

    args = parser.parse_args()
    if args.settings:
        set_environ('CONFIG', args.settings)


    settings = Settings()

    app_settings = {
        'template_path': settings.TEMPLATE_PATH,
        'static_path': settings.STATIC_PATH,
        'debug': settings.DEBUG,
    }

    application = tornado.web.Application(
        [
            (r"/static/(.*)", tornado.web.StaticFileHandler),
            (r"/", AuthLoginHandler, None, "home"),
            (r"/auth/login/", AuthLoginHandler, None, "login"),
            (r"/auth/exchange", ExchangeHandler, None, "exchange"),
        ], **app_settings)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(settings.APP_PORT_NUMBER)

    tornado.ioloop.IOLoop.instance().start()