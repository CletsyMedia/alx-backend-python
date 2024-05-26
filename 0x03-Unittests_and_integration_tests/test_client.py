#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.GithubOrgClient._session.get')
    def test_org(self, org_name, mock_get):
        test_response_json = {'key': 'value'}  # Sample response JSON
        mock_get.return_value.json.return_value = test_response_json

        # Call the method being tested
        org_client = GithubOrgClient(org_name)
        org_response = org_client.org()

        # Assertions
        self.assertEqual(org_response, test_response_json)
        mock_get.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
