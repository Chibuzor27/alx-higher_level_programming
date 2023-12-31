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

    def test_update_nil(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update()
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_id(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_width(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(20, 30)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_height(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(20, 30, 40)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_x(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(20, 30, 40, 50)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 1)

    def test_update_y(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(20, 30, 40, 50, 60)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 60)

    def test_update_extra(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(20, 30, 40, 50, 60, 70)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 60)

    def test_update_attr_id(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(id=20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_attr_width(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(width=20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_attr_height(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(height=20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_update_attr_x(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(x=20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 1)

    def test_update_attr_y(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(y=20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 20)

    def test_update_attr_all(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(id=20, height=20, width=20, x=20, y=20, unknown=20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 20)

    def test_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 4)
        self.assertEqual(r.to_dictionary(), {'\
id': 4, 'width': 10, 'height': 2, 'x': 1, 'y': 9})


if __name__ == "__main__":
    unittest.main()
