#!/usr/bin/env python3
"""
simple module to test functions in utils.py
using unittest module
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Testclass inherents the unittest.TestCase module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ({"a": {"b": 2}}, ("a", "b", "c"), KeyError),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping[str, Any],
                               path: Sequence[str],
                               expected_result: Any):
        """
        teting the access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "a"),
        ({"a": 1}, ("a", "b"), KeyError, "b"),
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping[str, Any],
                                         path: Sequence[str],
                                         expected_exception_message: str):
        """
        testing access_nested_map_exception
        """
        with self.assertRaisesRegex(KeyError, expected_exception_message):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class for utils.get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that utils.get_json returns expected result and
        requests.get is called once with correct url
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
