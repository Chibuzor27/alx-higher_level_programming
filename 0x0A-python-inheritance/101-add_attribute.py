#!/usr/bin/python3
"""Module"""


def add_attribute(my_class, attr, value):
    """Add attribute"""
    if not hasattr(my_class, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(my_class, attr, value)
