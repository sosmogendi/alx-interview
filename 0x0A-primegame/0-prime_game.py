#!/usr/bin/python3

def generate_primes(n):
    """Generate a list of prime numbers up to n using Sieve of Eratosthenes algorithm."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]


def isWinner(x, nums):
    """
    Determine the winner of each round based on the rules provided.
    :param x: Number of rounds
    :param nums: An array of n for each round
    :return: Name of the player that won the most rounds, or None if winner cannot be determined
    """
    def can_player_win(n, primes):
        if n < 2:
            return False
        if n in primes:
            return True
        if n % 2 == 0:
            return False
        return True

    max_num = max(nums)
    primes = generate_primes(max_num)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_player_win(n, primes):
            if n % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
