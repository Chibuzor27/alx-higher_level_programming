#!/usr/bin/python3
"""Unit test for base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit test for base"""

    def test_constructor(self):
        base = Base()
        self.assertEqual(base.id, 1)

        base = Base()
        self.assertEqual(base.id, 2)

    def test_constructor_withValue(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_to_dictionaries_json(self):
        base = Base()
        dic = {'x': 2, 'width': 10}
        self.assertEqual(Base.to_json_string(dic), '{"x": 2, "width": 10}')


if __name__ == '__main__':
    unittest.main()
