#!/usr/bin/env python3
"""
Unit tests for utils.py
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with various inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self, nested_map, path
    ):
        """
        Test access_nested_map raises KeyError for invalid paths
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test cases for get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        """
        Test get_json returns expected result
        """
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response

        self.assertEqual(get_json(url), payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """
    Test cases for memoize decorator
    """
    def test_memoize(self):
        """
        Test memoize works as expected
        """
        class TestClass:
            def __init__(self):
                self.call_count = 0

            @memoize
            def a_method(self):
                self.call_count += 1
                return self.call_count

        obj = TestClass()
        self.assertEqual(obj.a_method, 1)
        self.assertEqual(obj.a_method, 1)
        self.assertEqual(obj.call_count, 1)

        obj2 = TestClass()
        self.assertEqual(obj2.a_method, 1)
        self.assertEqual(obj2.a_method, 1)
        self.assertEqual(obj2.call_count, 1)


if __name__ == '__main__':
    unittest.main()
