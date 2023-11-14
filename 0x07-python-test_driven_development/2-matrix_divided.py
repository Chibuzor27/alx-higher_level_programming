#!/usr/bin/python3
"""Matrix module"""


def matrix_divided(matrix, div):
    """divide matrix"""
    if div is None or type(div) != int:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if matrix is None:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if len(matrix) > 0:
        width = -1
        hasValue = 0
        res = []
        for i in range(0, len(matrix)):
            if i == 0:
                width = len(matrix[i])
            else:
                if len(matrix[i]) != width:
                    raise TypeError('Each row of the matrix \
must have the same size')
            if width == 0:
                continue

            c = []
            for j in range(0, len(matrix[i])):
                if type(matrix[i][j]) is int or type(matrix[i][j]) is float:
                    val = matrix[i][j]/div
                    if (matrix[i][j] % div != 0 or div < 0):
                        c.append(round(val, 2))
                    else:
                        c.append(int(val))
                else:
                    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            res.append(c)
            hasValue = 1
        if hasValue == 1:
            return res
    return matrix
