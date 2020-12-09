#!/usr/bin/env python3
"""
Sigma of í square
"""


def summation_i_squared(n):
    """ that calculates operation """
    if type(n) is not int:
        return None
    elif type(n) is int and n <= 0:
        return sum((map(lambda res: res ** 2, range(1, n+1))))
