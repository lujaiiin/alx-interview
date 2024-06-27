#!/usr/bin/python3
"""modules"""


def island_perimeter(grid):
    """ fun """
    count = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1 if i == 0 else not grid[i - 1][j]
                count += 1 if i == rows - 1 else not grid[i + 1][j]
                count += 1 if j == 0 else not grid[i][j - 1]
                count += 1 if j == cols - 1 else not grid[i][j + 1]
    return count
