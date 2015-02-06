# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import tornado.ioloop
import tornado.web
import tornado.httpserver

from handlers.auth_handler import AuthHandler

if __name__ == '__main__':
    application = tornado.web.Application([
        (r"/", AuthHandler)
    ])