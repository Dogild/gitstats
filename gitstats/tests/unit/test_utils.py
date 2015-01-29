# -*- coding: utf-8 -*-

from datetime import date
from unittest import TestCase

from gitstats.lib.utils import transform_url

class UtilsTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method_transform_utils_with_simple_url(self):
        """Test the method transform_url with a simple url as https://api.github.com"""

        url = transform_url("https://api.github.com")
        assert url == "https://api.github.com"

    def test_method_transform_utils_with_simple_url_ending_with_slash(self):
        """Test the method transform_url with a simple url as https://api.github.com/"""

        url = transform_url("https://api.github.com/")
        assert url == "https://api.github.com"

    def test_method_transform_utils_with_api_url(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories"""

        url = transform_url("https://api.github.com/users/213/repositories")
        assert url == "https://api.github.com/users/213/repositories"

    def test_method_transform_utils_with_sha_url(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories/{123124214}"""

        url = transform_url("https://api.github.com/users/213/repositories/{123124214}")
        assert url == "https://api.github.com/users/213/repositories"

    def test_method_transform_utils_with_api_url_ending_with_slash(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories/"""

        url = transform_url("https://api.github.com/users/213/repositories/")
        assert url == "https://api.github.com/users/213/repositories"

    def test_method_transform_utils_with_sha_ur_ending_with_slash(self):
        """Test the method transform_url with a simple url as https://api.github.com/users/213/repositories/{123124214}/"""

        url = transform_url("https://api.github.com/users/213/repositories/{123124214}/")
        assert url == "https://api.github.com/users/213/repositories"

    def test_method_transform_utils_with_empty_url(self):
        """Test the method transform_url with a empty string"""

        url = transform_url("")
        assert url == ""
