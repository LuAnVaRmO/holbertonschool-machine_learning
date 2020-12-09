#!/usr/bin/env python3
"""Function that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial
    """
    if type(poly) is not list or len(poly) is 0 or poly is None \
            or type(C) not in (int, float) or C is None:
        return None
    npoly = [C]
    for i, c in enumerate(poly):
        if c % (i + 1) == 0:
            npoly.append(c // (i + 1))
        else:
            npoly.append(c / (i + 1))
    return npoly
