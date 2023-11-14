#!/usr/bin/python3
"""Matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """2-dimensional matrix multiplication"""

    if type(m_a) != list:
        raise TypeError('m_a must be a list')

    if type(m_b) != list:
        raise TypeError('m_b must be a list')

    if len(m_a) == 0:
        raise ValueError('m_a can\'t be empty')

    if len(m_b) == 0:
        raise ValueError('m_b can\'t be empty')

    rowsA = len(m_a)
    rowsB = len(m_b)

    if (type(m_a[0]) != list):
        raise TypeError('m_a must be a list of lists')

    if (type(m_b[0]) != list):
        raise TypeError('m_b must be a list of lists')

    colsA = len(m_a[0])
    colsB = len(m_b[0])

    if colsA == 0:
        raise ValueError('m_a can\'t be empty')

    if colsB == 0:
        raise ValueError('m_b can\'t be empty')

    for i in range(0, rowsA):
        if (type(m_a[i]) != list):
            raise TypeError('m_a must be a list of lists')

        if (len(m_a[i]) != colsA):
            raise TypeError('each row of m_a must be of the same size')

    for i in range(0, rowsB):
        if (type(m_b[i]) != list):
            raise TypeError('m_b must be a list of lists')

        if (len(m_b[i]) != colsB):
            raise TypeError('each row of m_b must be of the same size')

    if colsA != rowsB:
        raise ValueError('m_a and m_b can\'t be multiplied')

    mat = []
    for i in range(0, rowsA):
        res = []
        s = 0
        for j in range(0, colsB):
            s = 0
            for k in range(0, rowsB):
                if type(m_a[i][k]) != int and type(m_a[i][k]) != float:
                    raise TypeError('\
m_a should contain only integers or floats')
                if type(m_b[k][j]) != int and type(m_b[k][j]) != float:
                    raise TypeError('\
m_b should contain only integers or floats')
                s += m_a[i][k] * m_b[k][j]
            res.append(s)
        mat.append(res)
    return mat
