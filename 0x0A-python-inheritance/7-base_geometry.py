#!/usr/bin/python3
"""Module"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
