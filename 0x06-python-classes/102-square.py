#!/usr/bin/python3
"""Classes"""


class Square:
    """Square"""
    __size = 0

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) != int:
            raise ValueError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def __eq__(self, other):
        """Equal comparison"""
        return self.size == other.size

    def __ne__(self, other):
        """Not equal comparison"""
        return self.size != other.size

    def __lt__(self, other):
        """Less than comparison"""
        return self.size < other.size

    def __le__(self, other):
        """Less than or equal comparison"""
        return self.size <= other.size

    def __gt__(self, other):
        """Greater than comparison"""
        return self.size > other.size

    def __ge__(self, other):
        """Greater than or equal comparison"""
        return self.size >= other.size
