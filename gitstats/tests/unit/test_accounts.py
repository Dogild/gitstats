# -*- coding: utf-8 -*-

import responses

from datetime import date
from unittest import TestCase

from gitstats.models.account import Account, AccountNameException
from gitstats.tests.unit import bodies

class AccountTests(TestCase):

    def setUp(self):
        responses.add(responses.GET, 'https://api.github.com/users/little-dude?per_page=100',
                          body=bodies["https://api.github.com/users/little-dude?per_page=100"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

        responses.add(responses.GET, 'https://api.github.com/users/Dogil?per_page=100',
                          body=bodies["https://api.github.com/users/Dogil?per_page=100"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

        responses.add(responses.GET, 'https://api.github.com/users/little-dude/orgs?per_page=100',
                          body=bodies["https://api.github.com/users/little-dude/orgs?per_page=100"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

        responses.add(responses.GET, 'https://api.github.com/users/Dogild/orgs?per_page=100',
                          body=bodies["https://api.github.com/users/Dogild/orgs?per_page=100"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

        responses.add(responses.GET, 'https://api.github.com/orgs/cappuccino/repos?per_page=100',
                          body=bodies["https://api.github.com/orgs/cappuccino/repos?per_page=100"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

        responses.add(responses.GET, 'https://api.github.com/orgs/little-dude/repos?per_page=100',
                          body=bodies["https://api.github.com/orgs/little-dude/repos?per_page=100"],
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

    @responses.activate
    def test_method_get_users_bad_nickname(self):
        """Test the method _get_user"""
        account = Account("Dogil")

        with self.assertRaises(AccountNameException):
            account._get_users(uri="https://api.github.com/users/Dogil")

    @responses.activate
    def test_method_get_orgs(self):
        """Test the method _get_orgs"""
        account = Account("little-dude")
        account._get_orgs(uri="https://api.github.com/users/little-dude/orgs?per_page=100", fetcher=account.orgs)

        self.assertEqual(len(account.orgs), 2)
        self.assertEqual(account.orgs[0]["repos_url"], "https://api.github.com/orgs/cappuccino/repos")
        self.assertEqual(account.orgs[1]["repos_url"], "https://api.github.com/orgs/ArchipelProject/repos")

    @responses.activate
    def test_method_get_orgs_without_orgs(self):
        """Test the method _get_orgs"""
        account = Account("Dogild")
        account._get_orgs(uri="https://api.github.com/users/Dogild/orgs?per_page=100", fetcher=account.orgs)

        self.assertEqual(len(account.orgs), 0)

    @responses.activate
    def test_method_get_repos(self):
        """Test the method _get_repositories"""

        repositories = list()
        account = Account("little-dude")
        account._get_repositories(uri="https://api.github.com/orgs/cappuccino/repos?per_page=100", fetcher=repositories)

        self.assertEqual(len(repositories), 2)
        self.assertEqual(repositories[0]["name"], "cappuccino")
        self.assertEqual(repositories[1]["name"], "ojunit")

    @responses.activate
    def test_method_get_repos_without_repos(self):
        """Test the method _get_repositories"""

        repositories = list()
        account = Account("little-dude")
        account._get_repositories(uri="https://api.github.com/orgs/little-dude/repos?per_page=100", fetcher=repositories)

        self.assertEqual(len(repositories), 0)


