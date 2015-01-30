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

        account = Account("Dogild")

        assert account.user.name == "Dogild"
        assert account.repositories == list()
        assert account.forks == list()
        assert account.orgs == list()
        assert account.contributions == list()
        assert account.total_contributions == 0
        assert account.end_date.strftime("%c") == self.today.strftime("%c")
        assert account.start_date.strftime("%c") == (self.today - datetime.timedelta(days=364)).strftime("%c")

    def test_creation_commit(self):
        """Test the creation of a commit"""

        commit = Commit(date=self.today, sha="1234", author="Dogild", message="Fixed: unit test")

        assert commit.date.strftime("%c") == self.today.strftime("%c")
        assert commit.sha == "1234"
        assert commit.author == "Dogild"
        assert commit.message == "Fixed: unit test"

    def test_creation_repository(self):
        """Test the creation of a repository"""

        repository = Repository(name="gitstats", fork="dogild/gitstats", owner="Dogild", commits_url="http://github.com/Dogild/commits",  repos_url="http://github.com/Dogild/commits",  issues_url="http://github.com/Dogild/commits")

        assert repository.name == "gitstats"
        assert repository.fork == "dogild/gitstats"
        assert repository.owner == "Dogild"
        assert repository.commits_url == "http://github.com/Dogild/commits"
        assert repository.repos_url == "http://github.com/Dogild/commits"
        assert repository.issues_url == "http://github.com/Dogild/commits"
        assert repository.commits == list()

    def test_creation_issue(self):
        """Test the creation of an issue"""

        issue = Issue(date=self.today, number="1234", author="Dogild", title="Issue: unit test")

        assert issue.date == self.today
        assert issue.number == "1234"
        assert issue.author == "Dogild"
        assert issue.title == "Issue: unit test"

    def test_creation_user(self):
        """Test the creation of an user"""

        user = User(name="Dogild", repos_url="http://github.com/Dogild")

        assert user.name == "Dogild"
        assert user.repos_url == "http://github.com/Dogild"