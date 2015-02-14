# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Jonas Ghyllebert
# All Rights Reserved.
import unittest

from nose.tools import assert_equal

from strava.connection import StravaConnection


class StravaConnectionTestCase(unittest.TestCase):

    def test_authentication_url_no_extra_fields(self):
        connection = StravaConnection(9)

        expected_result = ("https://www.strava.com/oauth/authorize?"
                           "response_type=code&client_id=9&redirect_uri="
                           "http://127.0.0.1:8000/token")

        assert_equal(
            expected_result,
            connection.authentication_url(
                redirect_url='http://127.0.0.1:8000/token')
        )

    def test_authentication_url_extra_fields_uppercase(self):
        connection = StravaConnection(9)

        expected_result = ("https://www.strava.com/oauth/authorize?"
                           "response_type=code&client_id=9&redirect_uri="
                           "http://127.0.0.1:8000/token&bla=true")

        assert_equal(
            expected_result,
            connection.authentication_url(
                redirect_url='http://127.0.0.1:8000/token',
                bla="TRUE")
        )

    def test_authentication_url_extra_fields_unicode(self):
        connection = StravaConnection(9)

        expected_result = ("https://www.strava.com/oauth/authorize?"
                           "response_type=code&client_id=9&redirect_uri="
                           "http://127.0.0.1:8000/token&bla=%C3%BCbercool")

        assert_equal(
            expected_result,
            connection.authentication_url(
                redirect_url='http://127.0.0.1:8000/token',
                bla=u"übercool")
        )

    def test_exchange_token_url(self):
        connection = StravaConnection(9)
        token = "8a89044f305dd40778906c1ae01a7a2ed4cbace5"

        expected_result = ("https://www.strava.com/oauth/token?client_id=9"
                           "&code=8a89044f305dd40778906c1ae01a7a2ed4cbace5"
                           "&client_secret=s3cr31c0d3")

        assert_equal(
            expected_result,
            connection.exchange_token_url(token, "s3cr31c0d3")
        )