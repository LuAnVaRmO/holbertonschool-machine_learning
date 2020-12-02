#!/usr/bin/env python3
""" Matrix Shape """


def matrix_shape(matrix):
    """ Get the shape of a matrix """
    arr = []
    if type(matrix) is list:
        arr.append(len(matrix))
        arr += matrix_shape(matrix[0])
    return arr
