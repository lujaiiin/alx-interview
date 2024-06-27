#!/usr/bin/python3
"""modules"""


def makeChange(coins, total):
    """func"""

    if total < 1:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total

    for coin in coins:
        num_coins += remaining_total
        remaining_total = remaining_total % coin

    if remaining_total != 0:
        return -1

    return num_coins
