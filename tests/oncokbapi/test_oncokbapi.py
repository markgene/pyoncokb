"""Test OncokbApi class."""

import unittest

from pyoncokb.oncokbapi import OncokbApi


class OncokbApiTestCase(unittest.TestCase):
    """Test OncokbApi class."""

    def test_init(self):
        """Test initialization of OncokbApi instance."""
        oncokb_api = OncokbApi(auth="MOCKED")
        self.assertTrue(isinstance(oncokb_api, OncokbApi))
