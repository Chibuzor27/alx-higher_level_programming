#!/usr/bin/python3
def pow(a, b):
    n = 1
    r = b
    if b < 0:
        r = b * (-1)
    for i in range(0, r):
        if b < 0:
            n = n / (a * (-1))
        else:
            n = n * a
    return n
