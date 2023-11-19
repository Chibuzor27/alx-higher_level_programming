#!/usr/bin/python3
"""Module"""


def inherits_from(obj, a_class):
    """Inherits from"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
