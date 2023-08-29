#!/usr/bin/python3
"""Classes"""


class Square:
    """Square"""
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """Area"""
        return self.__size * self.__size

    def my_print(self):
        """Print"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                if (self.__position[0] > 0):
                    for k in range(0, self.__position[0]):
                        print(' ', end="")
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

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""

        if (isinstance(value, tuple) and len(value) == 2 and
                type(value[0]) == int and value[0] >= 0 and
                type(value[1]) == int and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
