#!/usr/bin/env python3
""" Matrix Shape """


def matrix_shape(matrix):
    """ Get the shape of a matrix """
    arr = [len(matrix), len(matrix[0])]
    if len(matrix[0]) > 2:
        arr.append(len(matrix[0][0]))
    return arr
