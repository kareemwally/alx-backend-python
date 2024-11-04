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
        ({}, ("a",), "key 'a' not found in {}"),
        ({"a": 1}, ("a", "b"), "key 'b' not found in {'a': 1}"),
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


if __name__ == '__main__':
    unittest.main()
