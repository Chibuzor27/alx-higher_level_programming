#!/usr/bin/python3
"""Print module"""


def say_my_name(first_name, last_name=""):
    """Print my name"""

    if first_name is None or type(first_name) != str:
        raise TypeError('first_name must be a string')

    if not (last_name is None or last_name is "") and type(last_name) != str:
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(
        first_name, "" if last_name is None else last_name))
