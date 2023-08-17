#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        m = 0
        for value in a_dictionary.values():
            if value > m:
                m = value
        return m
    else:
        return None
