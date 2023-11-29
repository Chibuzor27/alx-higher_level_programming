#!/usr/bin/python3
"""Rectangle tests"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for rectangle"""

    def test_parameterless_constructor(self):
        r = Rectangle(1, 1)
        self.assertEqual(r.id, Rectangle._Base__nb_objects)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 1)

    def test_constructor(self):
        r = Rectangle(1, 2, 3, 4, 20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("x", 1)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 1)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "x")

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -1)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, "x", 1)

    def test_zero_x(self):
        r = Rectangle(1, 1, 0, 1)
        self.assertEqual(r.x, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -1, 1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, "x")

    def test_zero_y(self):
        r = Rectangle(1, 1, 1, 0)
        self.assertEqual(r.y, 0)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        r = Rectangle(2, 5)
        self.assertEqual(r.area(), 10)

    def test_string(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")


if __name__ == "__main__":
    unittest.main()
