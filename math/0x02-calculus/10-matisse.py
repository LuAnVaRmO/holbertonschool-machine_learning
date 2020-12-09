#!/usr/bin/env python3
"""
Calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """ Calculates the derivative of a polynomial """
    if type(poly) != list:
        return None
    size = len(poly)
    if size == 0:
        return None
    for e in poly:
        if not isinstance(e, (int, float)):
            return None
    if size == 1:
        return [0]
    deriv = []
    for i in range(1, size):
        temp = poly[i] * i
        deriv.append(temp)
    return deriv
