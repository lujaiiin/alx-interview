#!/usr/bin/python3
"""Modules"""


def minOperations(n):
    """method that calculates the fewest number"""

    if n <= 0:
        return 0
    lenght = 1
    h = 1
    operation = 0

    while h < n:
        if n % h == 0:
            lenght = h
            operation = operation + 1
        h = h + lenght
        operation = operation + 1
    return operation
