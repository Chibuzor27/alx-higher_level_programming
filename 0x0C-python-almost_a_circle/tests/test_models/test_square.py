#!/usr/bin/python3
"""Square tests"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for squaree"""

    def test_parameterless_constructor(self):
        r = Square(1)
        self.assertEqual(r.id, Square._Base__nb_objects)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 1)

    def test_constructor(self):
        r = Square(1, 3, 4, 20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            r = Square("x")

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            r = Square(0)

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            r = Square(-1)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            r = Square(1, "x", 1)

    def test_zero_x(self):
        r = Square(1, 0, 1)
        self.assertEqual(r.x, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            r = Square(1, -1, 1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            r = Square(1, 1, "x")

    def test_zero_y(self):
        r = Square(1, 1, 0)
        self.assertEqual(r.y, 0)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            r = Square(1, 1, -1)

    def test_area(self):
        r = Square(2)
        self.assertEqual(r.area(), 4)

    def test_string(self):
        r = Square(2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Square] (5) 3/4 - 2")

    def test_update_nil(self):
        r = Square(1, 1, 1, 10)
        r.update()
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_id(self):
        r = Square(1, 1, 1, 10)
        r.update(20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_width(self):
        r = Square(1, 1, 1, 10)
        r.update(20, 30)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_x(self):
        r = Square(1, 1, 1, 10)
        r.update(20, 30, 50)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 1)

    def test_update_y(self):
        r = Square(1, 1, 1, 10)
        r.update(20, 30, 50, 60)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 60)

    def test_update_extra(self):
        r = Square(1, 1, 1, 10)
        r.update(20, 30, 50, 60, 70)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 60)

    def test_update_attr_id(self):
        r = Square(1, 1, 1, 10)
        r.update(id=20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_attr_width(self):
        r = Square(1, 1, 1, 10)
        r.update(width=20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_attr_x(self):
        r = Square(1, 1, 1, 10)
        r.update(x=20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 1)

    def test_update_attr_y(self):
        r = Square(1, 1, 1, 10)
        r.update(y=20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 20)

    def test_update_attr_all(self):
        r = Square(1, 1, 1, 10)
        r.update(id=20, width=20, x=20, y=20, unknown=20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 20)


if __name__ == "__main__":
    unittest.main()
