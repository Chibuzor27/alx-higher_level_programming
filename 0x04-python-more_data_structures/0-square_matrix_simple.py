#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        s = []
        for j in range(0, len(matrix[i])):
            s.append(matrix[i][j]**2)
        new_matrix.append(s)
    return new_matrix
