#!/usr/bin/python3
"""Module"""


def pascal_triangle(n):
    """Pascal triangle"""
    if type(n) != int:
        raise TypeError('n must be an integer')

    if n <= 0:
        return []

    mat = []
    s = ""
    for i in range(0, n):
        cur = []
        for x in range(0, i+1):
            if i == 0 or x == 0 or x == i:
                cur.append(1)
            else:
                item = mat[i-1][x-1] + mat[i-1][x]
                cur.append(item)
        mat.append(cur)
    return mat
