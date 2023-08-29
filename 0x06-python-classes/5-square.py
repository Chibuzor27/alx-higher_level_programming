#!/usr/bin/python3
"""Classes"""


class Square:
    """Square"""
    __size = 0

    def __init__(self, size=0):
        if type(size) != int:
            raise ValueError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Area"""
        return self.__size * self.__size

    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end="")
            print()

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
