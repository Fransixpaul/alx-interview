#!/usr/bin/python3
"""
Determine the fewest number of coins needed to make the total
using a combined greedy and dynamic programming approach.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # sort coins ina desending order for the greedy approach
    coins.sort(reverse=True)

    # Greedy approach
    greedy_total = total
    greedy_count = 0
    for coin in coins:
        if greedy_total == 0:
            break
        greedy_count += greedy_total // coin
        greedy_total %= coin

    # if greedy succeeds, return the result
    if greedy_total == 0:
        return greedy_count

    # Fall back to dynamic programming if greedy fails
    # Initialize DP table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0   # Base case

    # compute minimun coins for each amount up to total
    for x in range(1, total + 1):
        for coin in coins:
            if x - coin >= 0:
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # Return the result of DP, or -1 if the total cannot be reached
    return dp[total] if dp[total] != float('inf') else -1
