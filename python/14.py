# https://projecteuler.net/problem=14
# Longest Collatz sequence


# returns the length of the Collatz sequence having n as starting number
def collatz_seq_length(n):
    length = 1 # first in sequence is n
    if isinstance(n, int):
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = n * 3 + 1
            length += 1
    return length


def longest_collatz_seq_under(n):
    max_seq_length = 0
    solution = n
    while n > 0:
        current_length = collatz_seq_length(n)
        if current_length > max_seq_length:
            max_seq_length = current_length
            solution = n
        n -= 1
    return max_seq_length, solution

print longest_collatz_seq_under(1000000)
