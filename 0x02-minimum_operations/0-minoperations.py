#!/usr/bin/python3
"""Modules"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Parameters:
    - n (int): The target number of H characters.

    Returns:
    - int: The minimum number of operations needed to achieve n H characters, or 0 if it's impossible.
    """
    # Base case: If n is less than or equal to 1, it's impossible to achieve n H characters
    if n <= 1:
        return 0

    # Initialize a list to store the minimum number of operations for each number of H characters
    dp = [0] * (n + 1)

    # The minimum number of operations to reach 1 H character is 1 (Copy All)
    dp[1] = 1

    # Iterate through each number of H characters from 2 to n
    for i in range(2, n + 1):
        # The minimum number of operations to reach i H characters is either
        # 1 operation more than the minimum to reach i-1 H characters (Paste),
        # or 2 operations more than the minimum to reach i-2 H characters (Copy All and Paste).
        dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 2)

    # Return the minimum number of operations to reach n H characters
    return dp[n]
