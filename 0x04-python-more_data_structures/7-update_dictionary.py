#!/bin/usr/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    for x in a_dictionary.keys():
        if key == x:
            a_dictionary[x] = value
    return a_dictionary
