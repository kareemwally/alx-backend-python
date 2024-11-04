#!/usr/bin/env python3
"""
simple module to test functions in utils.py
using unittest module
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Mapping, Sequence, Any, Union
from utils import access_nested_map
from utils import memoize


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
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """
        Test that utils.get_json returns expected result and
        requests.get is called once with correct url
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test class for memoize decorator
    """
    def test_memoize(self) -> None:
        """
        Test that when calling a_property twice, the correct
        result is returned but a_method is only called once
        """
        class TestClass:
            """Test class for memoization"""
            def a_method(self) -> int:
                """Method to be memoized"""
                return 42

            @memoize
            def a_property(self) -> int:
                """Property that uses memoization"""
                return self.a_method()

        test_obj = TestClass()
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            first_call = test_obj.a_property
            second_call = test_obj.a_property

            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)
            mock_method.assert_called_once()


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name: str, mock_get_json) -> None:
        """
        Test that GithubOrgClient.org returns the correct value

        Args:
            org_name: name of the organization
            mock_get_json: mocked get_json method
        """
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == '__main__':
    unittest.main()
