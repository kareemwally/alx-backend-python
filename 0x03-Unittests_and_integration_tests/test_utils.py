#!/usr/bin/env python3
"""
simple module contain a test class inhereted from
unittest.TestCase
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Union


class TestAccessNestedMap(unittest.TestCase):
    """
    testing the access_nested_map function from utils
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
                               expected_result: Union[Any, type(Exception)]):
        """
        asserting the testcases from @parameterized.expand
        into function
        """
        if isinstance(expected_result, type) and issubclass(expected_result,
                                                            Exception):
            with self.assertRaises(expected_result):
                access_nested_map(nested_map, path)
        else:
            self.assertEqual(access_nested_map(nested_map, path),
                             expected_result)


if __name__ == '__main__':
    unittest.main()
