#!/usr/bin/python3
"""Add module"""


def add_integer(a, b=None):
    """Add integers"""
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError('a must be an integer')
    if b is None:
        return int(a)
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
