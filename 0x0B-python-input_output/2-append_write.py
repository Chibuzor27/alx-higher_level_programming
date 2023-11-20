#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """Write to file"""
    size = 0
    with open(filename, "a", encoding="utf-8") as f:
        size = f.write(text)
    return size
