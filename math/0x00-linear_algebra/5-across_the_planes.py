#!/usr/bin/python3
"""
Adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    newmat = []
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        for i in range(len(mat1)):
            temp = []
            for j in range(len(mat1[0])):
                temp.append(mat1[i][j] + mat2[i][j])
            newmat.append(temp)
        return newmat
    return None
