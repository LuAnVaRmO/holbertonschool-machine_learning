#!/usr/bin/env python3
""" Matrix Shape """
import numpy as np


def matrix_shape(matrix):
    """ Get the shape of a matrix """
    arr = np.array(matrix)
    return list(arr.shape)
