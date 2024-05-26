#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""

    @parameterized.expand([({},
                            ("a",
                             ),
                            KeyError,
                            "Key 'a' not found in nested_map"),
                           ({"a": 1},
                            ("a",
                             "b"),
                            KeyError,
                            "Key 'b' not found in nested_map['a']")])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_exception,
            expected_message):
        """Test access_nested_map function raises KeyError
        with expected message"""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
