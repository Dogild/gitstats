# -*- coding: utf-8 -*-

import responses

from datetime import date
from unittest import TestCase

from gitstats.models.account import Account
from gitstats.tests import bodies

class AccountTests(TestCase):

    def setUp(self):
        responses.add(responses.GET, 'https://api.github.com/users/little-dude?per_page=100',
                          body=bodies["https://api.github.com/users/little-dude?per_page=100"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

    def tearDown(self):
        pass

    @responses.activate
    def test_method_get_users(self):
        """Test the method _get_user"""
        account = Account("little-dude")
        account._get_users(uri="https://api.github.com/users/little-dude")

        self.assertEqual(account.user.repos_url, "https://api.github.com/users/little-dude/repos")