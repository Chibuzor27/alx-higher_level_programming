#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """Print square"""

    if size is None or (type(size) == float and size < 0):
        raise TypeError('size must be an integer')

    if type(size) != int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(0, size):
        for j in range(0, size):
            print('#', end="")
        print()
