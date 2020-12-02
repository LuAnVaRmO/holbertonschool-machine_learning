#!/usr/bin/env python3
"""
Performs element-wise addition, subtraction, multiplication, and division
"""


def np_elementwise(mat1, mat2):
    """ Performs element-wise adds, subs, mult, and divs """
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2

    return add, sub, mul, div
