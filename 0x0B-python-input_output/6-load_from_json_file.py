#!/usr/bin/python3
"""Module"""


import json


def load_from_json_file(filename):
    """Load from json file"""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
