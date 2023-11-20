#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """Write to file"""
    size = 0
    with open(filename, "w", encoding="utf-8") as f:
        size = f.write(text)
    return size
