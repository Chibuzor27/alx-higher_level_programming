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


if __name__ == "__main__":
    unittest.main()
