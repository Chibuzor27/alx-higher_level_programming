#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit test for max integer"""
    
    def test_default(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 4.2, "m"])

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_missing_param(self):
        self.assertEqual(max_integer(), None)

    def test_invalid_param(self):
        self.assertEqual(max_integer("az"), "z")

    def test_invalid_param(self):
        self.assertEqual(max_integer("za"), "z")

    def test_invalid_param(self):
        self.assertEqual(max_integer("aza"), "z")

if __name__ == '__main__':
    unittest.main()
