# Prime Game

## Description
This project implements the Prime Game, where Maria and Ben play rounds with a set of numbers. 
Players take turns selecting a prime number and removing it and its multiples from the set. 
The player who cannot make a move loses. The program determines the overall winner after 
`x` rounds.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 Style Guide (version 1.7.x)

## Usage
To determine the winner of the game, use the function `isWinner(x, nums)`:

```python
from 0-prime_game import isWinner

x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: Ben