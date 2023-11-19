#!/usr/bin/python3
"""Module"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Print sorted"""
        l = MyList(self)
        print(sorted(l))

    def __str__(self):
        """Print"""
        s = "["
        for i in range(0, len(self)):
            s = s + str(self[i])
            if i != len(self) - 1:
                s = s + ", "
        s = s + "]"
        return s
