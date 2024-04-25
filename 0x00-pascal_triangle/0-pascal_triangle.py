#!/usr/bin/python3
"""modules"""


def pascal_triangle(n):
    """ Pascal's Triangle """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        previous = tri[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        tri.append(current)
    return tri
