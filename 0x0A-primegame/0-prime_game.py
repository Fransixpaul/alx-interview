#!/usr/bin/python3
"""
Prime Game: Determines the winner of each round of the game.
Maria and Ben take turns choosing a prime number and removing it
and its multiples from the set. The player who cannot make a move loses.
"""


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the game.

    Args:
        x (int): Number of rounds.
        nums (list of int): List where each element is the maximum number n.

    Returns:
        str: Name of the player that won the most rounds (Maria or Ben),
             or None if the winner cannot be determined.
    """
    if x < 1 or not nums:
        return None

    # Find the maximum value in nums
    max_n = max(nums)

    # Precompute primes using the Sieve of Eratosthenes
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute winners for each possible n
    winner_for_n = {}
    for n in range(1, max_n + 1):
        primes = [i for i in range(1, n + 1) if is_prime[i]]
        maria_turn = True
        while primes:
            # Maria or Ben picks a prime and removes its multiples
            prime = primes[0]
            primes = [num for num in primes if num % prime != 0]
            maria_turn = not maria_turn  # Switch turns

        # Determine winner for this n
        winner_for_n[n] = "Ben" if maria_turn else "Maria"

    # Count wins for Maria and Ben
    maria_wins = sum(1 for n in nums if winner_for_n[n] == "Maria")
    ben_wins = x - maria_wins

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
