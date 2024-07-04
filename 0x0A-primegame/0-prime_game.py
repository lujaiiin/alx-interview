#!/usr/bin/python3
"""modules"""


def createSieveOfEratosthenes(limit):
    """
    Generates a boolean array marking primes up to limit.
    True indicates prime, False indicates composite.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, limit + 1, current):
                sieve[multiple] = False
    return sieve


def isWinner(x, nums):
    """func"""

    if x <= 0 or nums is None:
        return

    numsL = len(nums)
    primes = createSieveOfEratosthenes(max(nums))
    Maria = 0
    Ben = 0
    for round in range(x):
        valid = [n for n in range(2, nums[round % numsL] + 1) if primes[n]]
        if len(valid) % 2 == 1:
            Maria += 1
        else:
            Ben += 1
    if Ben == Maria:
        return
    elif Ben > Maria:
        return 'Ben'
    else:
        return 'Maria'
