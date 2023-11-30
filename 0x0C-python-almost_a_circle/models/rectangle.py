#!/usr/bin/python3
"""Rectangle module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name, value):
        """Validate parameter"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        self.validate("width", value)
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        self.validate("height", value)
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        self.validate("x", value)
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        self.validate("y", value)
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Calculate area"""
        return self.width * self.height

    def display(self):
        """Displa"""
        for i in range(0, self.height+self.y):
            if self.y > 0 and i < self.y:
                print()
                continue
            else:
                for j in range(0, self.width+self.x):
                    if self.x > 0 and j < self.x:
                        print(' ', end="")
                    else:
                        print('#', end="")
                print()

    def __str__(self):
        """String representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Update instance variables"""
        size = len(args)
        a = 0
        while a < size and a < 5:
            if a == 0:
                self.id = args[a]
            elif a == 1:
                self.width = args[a]
            elif a == 2:
                self.height = args[a]
            elif a == 3:
                self.x = args[a]
            elif a == 4:
                self.y = args[a]
            a = a + 1
