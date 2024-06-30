#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
import requests
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """Memoization"""
    def test_memoize(self):
        """test method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42

            instance = TestClass()

            res1 = instance.a_property
            res2 = instance.a_property

            mock_method.assert_called_once()

            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)


if __name__ == "__main__":
    unittest.main()
