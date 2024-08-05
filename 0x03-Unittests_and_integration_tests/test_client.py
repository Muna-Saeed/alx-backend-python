#!/usr/bin/env python3

# test_client.py
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, org_name, expected):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        with patch('client.GithubOrgClient.get_json', return_value=expected) as mock_get_json:
            org = client.org
            self.assertEqual(org, expected)
            mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
            
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url returns the expected value"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

if __name__ == "__main__":
    unittest.main()
