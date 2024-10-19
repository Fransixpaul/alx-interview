#!/usr/bin/python3
"""
Calculates the fewest number of operations
required to generate exactly n H characters
using only "Copy All" and "Paste"
"""


def minOperations(n):

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
