#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size"""
        self.validate("size", value)
        if value < 0:
            raise ValueError('size must be >= 0')
        self.width = value
        self.height = value

    def __str__(self):
        """String repre sentation"""
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update instance variables"""

        size = len(args)
        if size > 0:
            a = 0
            while a < size and a < 4:
                if a == 0:
                    self.id = args[a]
                elif a == 1:
                    self.size = args[a]
                elif a == 2:
                    self.x = args[a]
                elif a == 3:
                    self.y = args[a]
                a = a + 1
        else:
            if kwargs is not None:
                for (name, value) in kwargs.items():
                    setattr(self, name, value)
