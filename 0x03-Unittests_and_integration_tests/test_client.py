#!/usr/bin/env python3

"""
test_client.py

This module contains unit tests for the
GithubOrgClient class from the client module.
It includes tests for:
- The `org` property to ensure it returns the correct organization data.
- The `_public_repos_url` property to ensure it returns the correct URL.
- The `public_repos` method to ensure it
  returns the correct list of repositories.

The tests use the unittest framework along with patching and parameterized
decorators to mock external calls and validate functionality.
"""

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
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): The name of the organization.
            expected (dict): The expected response from the API.
            mock_get_json (MagicMock): Mocked get_json method.
        """
        client = GithubOrgClient(org_name)
        with patch(
            'client.GithubOrgClient.get_json', return_value=expected
          ) as mock_get_json:
            org = client.org
            self.assertEqual(org, expected)
            mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}'
            )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url
        returns the expected value

        Args:
            mock_org (MagicMock): Mocked org property.
        """
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result,
                         "https://api.github.com/orgs/google/repos"
                         )

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test that GithubOrgClient.public_repos
        returns the expected list of repos

        Args:
            mock_public_repos_url (MagicMock):
            Mocked _public_repos_url property.
            mock_get_json (MagicMock): Mocked get_json method.
        """
        mock_public_repos_url.return_value = {
                "https://api.github.com/orgs/google/repos"
                }
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        client = GithubOrgClient("google")
        result = client.public_repos()

        self.assertEqual(result, ["repo1", "repo2", "repo3"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos"
        )

    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license returns the expected
        result based on the repository's license.

        Args:
            repo (dict): The repository object with license information.
            license_key (str): The license key to check.
            expected (bool): The expected result.
        """
        client = GithubOrgClient("google")

        # Mock the repo method to return the provided repo dictionary
        with patch.object(client, 'repo', return_value=repo):
            result = client.has_license(license_key)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
