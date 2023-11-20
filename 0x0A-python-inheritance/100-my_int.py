#!/usr/bin/python3
"""Module"""


class MyInt(int):
    """My integer class"""
    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
