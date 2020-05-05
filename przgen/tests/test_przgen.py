import unittest
import pytest
from flask import abort, url_for
from flask_testing import TestCase
from application import app


class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        return app

class TestViews(TestBase):

    def test_chkcode(self):
        response = self.client.get(url_for('prize'))
        self.assertEqual("code" in response.json, True)

    def test_chkprize(self):
            response = self.client.get(url_for('prize'))
            self.assertEqual("prize" in response.json, True)