#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = {}
    for key, value in a_dictionary.items():
        n[key] = value * 2
    return n
