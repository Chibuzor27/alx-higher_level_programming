#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=0):
        if type(size) != int:
            raise ValueError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
