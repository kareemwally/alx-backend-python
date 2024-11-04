#!/usr/bin/env python3
"""
simple module contain a test class inhereted from
unittest.TestCase
"""
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    testing the access_nested_map function from utils
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        asserting the testcases from @parameterized.expand
        into function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__':
    unittest.main()
