# https://projecteuler.net/problem=10
# Summation of primes

from math import sqrt

import time

UNMARKED = 0
MULTIPLE = 1
PRIME = 2


def unmarked(x):
    return x == UNMARKED


def multiple(x):
    return x == MULTIPLE


def prime(x):
    return x == PRIME


# returns list of all primes up to 'upper_limit' param
def eratosthenes_sieve(upper_limit):
    numbers = [UNMARKED] * (upper_limit + 1) # start with all numbers unmarked, from 0 to upper_limit
    for a in range(2, int(sqrt(upper_limit)) + 1):
        if unmarked(numbers[a]):
            numbers[a] = PRIME
            for i in range(a ** 2, upper_limit + 1, a):
                numbers[i] = MULTIPLE
    return [index for index in range(len(numbers)) if numbers[index] == PRIME or (index > sqrt(upper_limit) and numbers[index] == UNMARKED) ]


primes = eratosthenes_sieve(2000000)
print sum(i for i in primes)
