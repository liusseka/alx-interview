#!/usr/bin/python3
"""
Define the isWinner function as a solution to the Prime Game problem.
"""


def primes(n):
    """
    Generate a list of prime numbers from 1 to n, inclusive.

    Args: n (int): the upper limit of the range, with the
    lower limit fixed at 1.
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
   Determines the winner of the Prime Game.

    Args: x (int): the number of rounds in the game nums (int):
    the upper limit of the range for each round

    Returns: The name of the winner (Maria or Ben),
    or None if no winner can be determined.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
