# -*- coding: utf-8 -*-

from datetime import date
from unittest import TestCase

from gitstats.lib.routes import make_uri_user, make_uri_search_issue, make_uri_orgs

class RoutesTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_route_user(self):
        """Test the route user, we should have https://api.github.com/users/Dogild"""

        url = make_uri_user("Dogild")
        self.assertEqual(url, "https://api.github.com/users/Dogild")

    def test_route_search_issue(self):
        """Test the route user, we should have https://api.github.com/search/issues"""

        url = make_uri_search_issue()
        self.assertEqual(url, "https://api.github.com/search/issues")

    def test_route_organization(self):
        """Test the route user, we should have https://api.github.com/users/Dogild/orgs"""

        url = make_uri_orgs("Dogild")
        self.assertEqual(url, "https://api.github.com/users/Dogild/orgs")