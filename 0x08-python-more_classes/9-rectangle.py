#!/usr/bin/python3
""" More Classes """


class Rectangle:
    """Rectangle"""
    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    def area(self):
        """Area"""
        return self.height * self.width

    def perimeter(self):
        """Perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Print string"""
        out = ""
        if self.height == 0 or self.width == 0:
            return out
        for i in range(0, self.height):
            for j in range(0, self.width):
                out = out + str(self.print_symbol)
            if (i != self.height - 1):
                out = out + '\n'
        return out

    def __repr__(self):
        """Repr"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Del"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
