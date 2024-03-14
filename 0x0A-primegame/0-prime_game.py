#!/usr/bin/python3

"""Prime Game Algorithm Python"""

def is_prime(n):
    """Check if a number n is prime"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_primes(n, primes):
    """Calculate all primes up to n and store in the primes list"""
    top_prime = primes[-1]
    if n > top_prime:
        for i in range(top_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)

def isWinner(x, nums):
    """
    Determine the winner of each round based on the rules provided.
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    players_wins = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]  # Initialize with first three primes

    calculate_primes(max(nums), primes)

    for num in nums:
        sum_options = sum(1 for p in primes[:num + 1] if p != 0)

        if sum_options % 2:
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
