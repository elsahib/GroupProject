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

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_loginview(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_registerview(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)
    
    #test for login required
    def test_account(self):
        response = self.client.get(url_for('account'))
        self.assertEqual(response.status_code, 302)

    def test_account(self):
            response = self.client.get(url_for('gen'))
            self.assertEqual(response.status_code, 302)

    def test_logout(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 302)

    def test_delete_account(self):
        response = self.client.get(url_for('account_delete'))
        self.assertEqual(response.status_code, 302)

    def test_account(self):
        response = self.client.get(url_for('account'))
        self.assertEqual(response.status_code, 302)

