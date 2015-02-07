# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import os
import importlib


def set_environ(key, value):
    os.environ[key] = str(value)


class Settings(object):

    def __init__(self):
        settings_module = os.environ.get('CONFIG', 'config.base')

        mod = importlib.import_module(settings_module)

        for setting in dir(mod):
            value = getattr(mod, setting)
            setattr(self, setting, value)


settings = Settings()