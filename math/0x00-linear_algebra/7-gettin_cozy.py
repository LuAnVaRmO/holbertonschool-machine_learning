#!/usr/bin/env python3
"""
Concatenates two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ That concatenates two matrices along a specific axis """
    c_mat1 = [row[:] for row in mat1]
    c_mat2 = [row[:] for row in mat2]
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        return c_mat1 + c_mat2
    elif axis == 1 and len(mat1) == len(mat2):
        newmat = []
        for i in range(len(mat1)):
            newmat.append(c_mat1[i] + c_mat2[i])
        return newmat
    return None
