#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for i in range(0, len(matrix)):
            if len(matrix[i]) > 0:
                for j in range(0, len(matrix[i])):
                    if j != 0:
                        print(" ", end="")
                    print('{:d}'.format(matrix[i][j]), end="")
                    if j == len(matrix[i]) - 1:
                        print("\n", end="")
            else:
                print()
