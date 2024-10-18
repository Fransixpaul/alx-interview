#!/usr/bin/python3
"""
This module defines a function to generate a pascal's Triangle.
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of size n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Start the new row with 1
        # Fill in the middle values using the previous row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)
    return triangle