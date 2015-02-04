# -*- coding: utf-8 -*-

from datetime import date
from unittest import TestCase

from gitstats.models.account import Account
from gitstats.models.commit import Commit
from gitstats.models.user import User
from gitstats.models.issue import Issue
from gitstats.models.repository import Repository

import datetime
import calendar
from datetime import timedelta, time

class ModelTests(TestCase):

    def setUp(self):
        self.today = datetime.datetime.today()

    def tearDown(self):
        pass

    def test_creation_account(self):
        """Test the creation of an account"""

        account = Account("Dogild", timezone=32400, token="abc")

        self.assertEqual(account.user.name, "Dogild")
        self.assertEqual(account.user.timezone, 32400)
        self.assertEqual(account.user.token, "abc")
        self.assertEqual(account.repositories, list())
        self.assertEqual(account.forks, list())
        self.assertEqual(account.orgs, list())
        self.assertEqual(account.contributions, list())
        self.assertEqual(account.total_contributions, 0)
        self.assertEqual(account.end_date.strftime("%c"), self.today.strftime("%c"))
        self.assertEqual(account.start_date.strftime("%c"), (self.today - datetime.timedelta(days=364)).strftime("%c"))

    def test_creation_commit(self):
        """Test the creation of a commit"""

        commit = Commit(date=self.today, sha="1234", author="Dogild", message="Fixed: unit test")

        self.assertEqual(commit.date.strftime("%c"), self.today.strftime("%c"))
        self.assertEqual(commit.sha, "1234")
        self.assertEqual(commit.author, "Dogild")
        self.assertEqual(commit.message, "Fixed: unit test")

    def test_creation_repository(self):
        """Test the creation of a repository"""

        repository = Repository(name="gitstats", fork="dogild/gitstats", owner="Dogild", commits_url="http://github.com/Dogild/commits",  repos_url="http://github.com/Dogild/commits",  issues_url="http://github.com/Dogild/commits")

        self.assertEqual(repository.name, "gitstats")
        self.assertEqual(repository.fork, "dogild/gitstats")
        self.assertEqual(repository.owner, "Dogild")
        self.assertEqual(repository.commits_url, "http://github.com/Dogild/commits")
        self.assertEqual(repository.repos_url, "http://github.com/Dogild/commits")
        self.assertEqual(repository.issues_url, "http://github.com/Dogild/commits")
        self.assertEqual(repository.commits, list())

    def test_creation_issue(self):
        """Test the creation of an issue"""

        issue = Issue(date=self.today, number="1234", author="Dogild", title="Issue: unit test")

        self.assertEqual(issue.date, self.today)
        self.assertEqual(issue.number, "1234")
        self.assertEqual(issue.author, "Dogild")
        self.assertEqual(issue.title, "Issue: unit test")

    def test_creation_user(self):
        """Test the creation of an user"""

        user = User(name="Dogild", timezone=32400, repos_url="http://github.com/Dogild", token="abc")

        self.assertEqual(user.name, "Dogild")
        self.assertEqual(user.timezone, 32400)
        self.assertEqual(user.token, "abc")
        self.assertEqual(user.repos_url, "http://github.com/Dogild")