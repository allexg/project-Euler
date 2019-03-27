# https://projecteuler.net/problem=7
# 10001st prime

from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def nthPrime(n):
    current = 2
    while n > 0:
        if is_prime(current):
            n -= 1
        current += 1
    return current - 1


print nthPrime(10001)
