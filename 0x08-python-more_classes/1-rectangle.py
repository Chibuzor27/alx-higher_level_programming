#!/usr/bin/python3
""" More Classes """


class Rectangle:
    """Rectangle"""
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Prop: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set prop: width"""
        if type(value) != int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Prop: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set prop: height"""
        if type(value) != int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
