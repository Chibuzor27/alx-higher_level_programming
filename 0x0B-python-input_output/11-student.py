#!/usr/bin/python3
"""Module"""


class Student:
    """Class student"""
    def __init__(self, firstname, lastname, age):
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            ml = {}
            for i in range(0, len(attrs)):
                if hasattr(self, attrs[i])\
                        and getattr(self, attrs[i]) is not None:
                    ml[attrs[i]] = getattr(self, attrs[i])
            return ml

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
