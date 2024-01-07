#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
from 6-max_integer_test.py import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test case for a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test case for a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Test case for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_mixed_types(self):
        """Test case for a list with mixed types"""
        self.assertEqual(max_integer([1, "hello", 3, 4]), 4)

    def test_single_element(self):
        """Test case for a list with a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_large_numbers(self):
        """Test case for a list with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 10000000]), 10000000)

    def test_float_numbers(self):
        """Test case for a list with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.3]), 3.3)

    def test_duplicate_values(self):
        """Test case for a list with duplicate maximum values"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()

