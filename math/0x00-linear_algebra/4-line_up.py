#!/usr/bin/env python3
"""
Adds two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """ Add arr1[i] + arr2[i] """
    arr = []
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            arr.append(arr1[i] + arr2[i])
        return arr
    return None
