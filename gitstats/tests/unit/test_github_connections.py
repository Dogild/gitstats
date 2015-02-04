# -*- coding: utf-8 -*-

from datetime import date
from unittest import TestCase

from gitstats.lib.github_connection import GithubConnection

class GithubConnectionTests(TestCase):

    def setUp(self):
        self.uri = "https://api.github.com/users/"

    def tearDown(self):
        pass

    def test_method_transform_utils_with_simple_url(self):
        """Test the method transform_url with a simple url as https://api.github.com"""

        github_connection = GithubConnection("Dogild")
        url = github_connection._transform_url("https://api.github.com")
        self.assertEqual(url, "https://api.github.com")

    def test_method_transform_utils_with_simple_url_ending_with_slash(self):
        """Test the method transform_url with a simple url as https://api.github.com/"""

        github_connection = GithubConnection("Dogild")
        url = github_connection._transform_url("https://api.github.com/")
        self.assertEqual(url, "https://api.github.com")

    def test_method_transform_utils_with_api_url(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories"""

        github_connection = GithubConnection("Dogild")
        url = github_connection._transform_url("https://api.github.com/users/213/repositories")
        self.assertEqual(url, "https://api.github.com/users/213/repositories")

    def test_method_transform_utils_with_sha_url(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories/{123124214}"""

        github_connection = GithubConnection("Dogild")
        url = github_connection._transform_url("https://api.github.com/users/213/repositories/{123124214}")
        self.assertEqual(url, "https://api.github.com/users/213/repositories")

    def test_method_transform_utils_with_api_url_ending_with_slash(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories/"""

        github_connection = GithubConnection("Dogild")
        url = github_connection._transform_url("https://api.github.com/users/213/repositories/")
        self.assertEqual(url, "https://api.github.com/users/213/repositories")

    def test_method_transform_utils_with_sha_ur_ending_with_slash(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories/{123124214}/"""

        github_connection = GithubConnection("Dogild")
        url = github_connection._transform_url("https://api.github.com/users/213/repositories/{123124214}/")
        self.assertEqual(url, "https://api.github.com/users/213/repositories")

    def test_method_transform_utils_with_empty_url(self):
        """Test the method transform_url with a empty string"""

        github_connection = GithubConnection("Dogild")
        url = github_connection._transform_url("")
        self.assertEqual(url, "")

    def test_method_add_params_with_no_param(self):
        """Test the method _add_params with no param, the method adds by default the param per_page=100"""

        github_connection = GithubConnection("Dogild")
        uri = github_connection._add_params(self.uri, dict())

        self.assertEqual(uri, "https://api.github.com/users?per_page=100")

    def test_method_add_params_with_param(self):
        """Test the method _add_params with param, the method adds by default the param per_page=100"""

        github_connection = GithubConnection("Dogild")
        params = dict()
        params["test"] = "32"
        uri = github_connection._add_params(self.uri, params)

        self.assertEqual(uri, "https://api.github.com/users?test=32&per_page=100")

    def test_method_add_params_with_params(self):
        """Test the method _add_params with params, the method adds by default the param per_page=100"""

        github_connection = GithubConnection("Dogild")
        params = dict()
        params["test"] = "32"
        params["nosetest"] = "coucou"
        uri = github_connection._add_params(self.uri, params)

        self.assertEqual(uri, "https://api.github.com/users?test=32&per_page=100&nosetest=coucou")