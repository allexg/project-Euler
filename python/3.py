# https://projecteuler.net/problem=3
# Largest prime factor
from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    for d in range(2, int(sqrt(number)) + 1):
        if number % d == 0:
            return False
    return True


def smallest_prime_factor(number):
    i = 2
    while i <= number:
        if is_prime(i) and number % i == 0:
            return i
        i += 1

# any integer can be written as a product of prime numbers
# dividing the number by its prime factors (in order, starting with the smallest)
# the latest division will be by the largest prime factor
def largest_prime_factor(number):
    while True:
        smallest_prime = smallest_prime_factor(number)
        if number / smallest_prime == 1:
            return number
        number /= smallest_prime


print largest_prime_factor(600851475143)
