# -*- coding: utf-8 -*-

import responses

from datetime import datetime
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

        responses.add(responses.GET, 'https://api.github.com/repos/cappuccino/ojtest/commits?per_page=100&since=2014-02-04T00:00:00.000001&until=2015-02-03T00:00:00.000001&author=little-dude',
                          body=bodies["https://api.github.com/repos/cappuccino/ojtest/commits?per_page=100&since=2014-02-04T00:00:00.000001&until=2015-02-03T00:00:00.000001&author=little-dude"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

        responses.add(responses.GET, 'https://api.github.com/repos/cappuccino/ojunit/commits?per_page=100&since=2014-02-04T00:00:00.000001&until=2015-02-03T00:00:00.000001&author=little-dude',
                          body=bodies["https://api.github.com/repos/cappuccino/ojunit/commits?per_page=100&since=2014-02-04T00:00:00.000001&until=2015-02-03T00:00:00.000001&author=little-dude"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

        responses.add(responses.GET, 'https://api.github.com/search/issues?q=author:little-dude&per_page=100',
                          body=bodies["https://api.github.com/search/issues?q=author:little-dude&per_page=100"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json',
                          adding_headers={"link": '<https://api.github.com/search/issues?q=author:little-dude&per_page=100&page=2>; rel="next"'})

        responses.add(responses.GET, 'https://api.github.com/search/issues?q=author:little-dude&per_page=100&page=2',
                          body=bodies["https://api.github.com/search/issues?q=author:little-dude&per_page=100&page=2"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json',
                          adding_headers={"link": '<https://api.github.com/search/issues?q=author:little-dude&per_page=100&page=3>; rel="next"'})

        responses.add(responses.GET, 'https://api.github.com/search/issues?q=author:little-dude&per_page=100&page=3',
                          body=bodies["https://api.github.com/search/issues?q=author:little-dude&per_page=100&page=3"],
                          status=200,
                          match_querystring=True,
                          content_type='application/json')

    def tearDown(self):
        pass

    @responses.activate
    def test_method_get_users(self):
        """Test the method _get_user"""
        account = Account("little-dude", timezone=32400)
        account._get_users(uri="https://api.github.com/users/little-dude")

        self.assertEqual(account.user.repos_url, "https://api.github.com/users/little-dude/repos")

    @responses.activate
    def test_method_get_users_bad_nickname(self):
        """Test the method _get_user"""
        account = Account("Dogil", timezone=32400)

        with self.assertRaises(AccountNameException):
            account._get_users(uri="https://api.github.com/users/Dogil")

    @responses.activate
    def test_method_get_orgs(self):
        """Test the method _get_orgs"""
        account = Account("little-dude", timezone=32400)
        account._get_orgs(uri="https://api.github.com/users/little-dude/orgs?per_page=100", fetcher=account.orgs)

        self.assertEqual(len(account.orgs), 2)
        self.assertEqual(account.orgs[0]["repos_url"], "https://api.github.com/orgs/cappuccino/repos")
        self.assertEqual(account.orgs[1]["repos_url"], "https://api.github.com/orgs/ArchipelProject/repos")

    @responses.activate
    def test_method_get_orgs_without_orgs(self):
        """Test the method _get_orgs"""
        account = Account("Dogild", timezone=32400)
        account._get_orgs(uri="https://api.github.com/users/Dogild/orgs?per_page=100", fetcher=account.orgs)

        self.assertEqual(len(account.orgs), 0)

    @responses.activate
    def test_method_get_repos(self):
        """Test the method _get_repositories"""

        repositories = list()
        account = Account("little-dude", timezone=32400)
        account._get_repositories(uri="https://api.github.com/orgs/cappuccino/repos?per_page=100", fetcher=repositories)

        self.assertEqual(len(repositories), 2)
        self.assertEqual(repositories[0]["name"], "cappuccino")
        self.assertEqual(repositories[1]["name"], "ojunit")

    @responses.activate
    def test_method_get_repos_without_repos(self):
        """Test the method _get_repositories"""

        repositories = list()
        account = Account("little-dude", timezone=32400)
        account._get_repositories(uri="https://api.github.com/orgs/little-dude/repos?per_page=100", fetcher=repositories)

        self.assertEqual(len(repositories), 0)

    @responses.activate
    def test_method_sync_user(self):
        """Test the method sync_user"""

        account = Account("little-dude", timezone=32400)
        account.sync_user_account()

        self.assertEqual(len(account.orgs), 2)
        self.assertEqual(account.orgs[0]["repos_url"], "https://api.github.com/orgs/cappuccino/repos")
        self.assertEqual(account.orgs[1]["repos_url"], "https://api.github.com/orgs/ArchipelProject/repos")

        self.assertEqual(account.user.repos_url, "https://api.github.com/users/little-dude/repos")

    @responses.activate
    def test_method_get_commits_for_repository(self):
        """Test the method _get_commits_for_repository"""
        account = Account("little-dude", timezone=32400)
        account.end_date = datetime(2015, 2, 3, 0, 0, 0, 1)
        account.start_date = datetime(2014, 2, 4, 0, 0, 0, 1)

        commits = list()
        account._get_commits_for_repository(uri="https://api.github.com/repos/cappuccino/ojtest/commits", fetcher=commits)

        self.assertEqual(len(commits), 2)

        self.assertEqual(str(commits[0]).replace('\n', ''), "Commit : 2014-08-04 14:47:35 Alexandre Wilhelm Fixed: removed double methods...")
        self.assertEqual(str(commits[1]).replace('\n', ''), "Commit : 2014-08-04 14:44:20 Alexandre Wilhelm New: Added the number of tests launchedPreviously, when a suite of tests ended, we didn't know how many tests were launched.Now we know. The formats of the message can be :-   All tests passed in the test suite.    Total tests: 176-   Test suite failed with 0 errors and 1 failures and 175 successes    Total tests : 176")

    @responses.activate
    def test_method_get_commits_for_repository_without_commit(self):
        """Test the method _get_commits_for_repository"""
        account = Account("little-dude", timezone=32400)
        account.end_date = datetime(2015, 2, 3, 0, 0, 0, 1)
        account.start_date = datetime(2014, 2, 4, 0, 0, 0, 1)

        commits = list()
        account._get_commits_for_repository(uri="https://api.github.com/repos/cappuccino/ojunit/commits", fetcher=commits)

        self.assertEqual(len(commits), 0)

    @responses.activate
    def test_method_search_issues(self):
        """Test the method search_issues"""
        account = Account("little-dude", timezone=32400)
        account.end_date = datetime(2015, 2, 3, 0, 0, 0, 1)
        account.start_date = datetime(2014, 2, 4, 0, 0, 0, 1)

        issues = list()
        account.get_issues(account.start_date, account.end_date, fetcher=issues)

        self.assertEqual(len(issues), 2)
        self.assertEqual(str(issues[0]).replace('\n', ''), "Issue 2015-01-02 10:14:05 : little-dude logs printed twice")
        self.assertEqual(str(issues[1]).replace('\n', ''), "Issue 2014-12-23 10:52:01 : little-dude Refactor loadTestsFromName in smaller bites.")


