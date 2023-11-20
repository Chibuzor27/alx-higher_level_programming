#!/usr/bin/python3
"""Module"""


import json


class Student:
    """Class student"""
    def __init__(self, firstname, lastname, age):
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self):
        return json.loads(json.dumps(self.__dict__))
