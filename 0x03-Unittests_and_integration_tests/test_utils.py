#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
import requests
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize unit testing pattern"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Testing the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self, n_map, path, expected):
        """
        Test access_nested_map raises
        KeyError with expected error message.
        """
        with self.assertRaises(KeyError, msg=expected):
            access_nested_map(n_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP Calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, payload, mock_get):
        """Mock testing"""
        mock_output = Mock()
        mock_output.json.return_value = payload

        mock_get.return_value = mock_output

        results = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(results, payload)


if __name__ == "__main__":
    unittest.main()
