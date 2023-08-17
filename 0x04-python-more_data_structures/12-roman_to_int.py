#!/usr/bin/python3
def roman_to_int(roman_string):
    st = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    s = 0
    for i in range(0, len(roman_string)):
        c = roman_string[i]
        if c in st:
            s = s + st[c]
    return s
