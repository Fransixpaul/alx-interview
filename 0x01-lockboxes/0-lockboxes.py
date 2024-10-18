#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be unlocked
based on the keys found in each box.
"""

def canUnlockAll(boxes):
    n= len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_key = keys.pop()

        for key in boxes[current_key]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
