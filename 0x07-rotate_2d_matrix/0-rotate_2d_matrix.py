#!/usr/bin/python3
"""modules"""


def rotate_2d_matrix(matrix):
    """rotate fun"""

    length = len(matrix)
    mid = int(length / 2)
    if length % 2 == 1:
        mid += 1
    for i in range(mid):
        for j in range(i, length - i - 1):
            high = length - 1
            top = matrix[i][j]
            left = matrix[high - j][i]
            bot = matrix[high - i][high - j]
            right = matrix[j][high - i]
            matrix[j][high - i], matrix[high - i][high - j] = top, right
            matrix[i][j], matrix[high - j][i] = left, bot
