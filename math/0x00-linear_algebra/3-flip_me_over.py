#!/usr/bin/python3
"""
Returns the transpose of a 2D matrix
"""


def matrix_transpose(matrix):
    """ Tanspose of a 2D matrix """
    arr = []
    for i in range(len(matrix[0])):
        inner = []
        for j in range(len(matrix)):
            inner.append(matrix[j][i])
        arr.append(inner)
    return arr
