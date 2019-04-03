# https://projecteuler.net/problem=12
# Highly divisible triangular number


def nb_divisors(n):
    if n < 2:
        return 1
    nb_div = 0
    for d in range(2, n/2 + 1):
        if n % d == 0:
            nb_div += 1
    return nb_div + 2 # take into account that n divides by 1 and by n

# for step n, triangular number is (n(n+1))/2. n and n+1 are coprimes, so their divisors are distinct => nb_divisors(n(n+1)) = nb(divisors(n) * nb_divisors(n+1)
def highly_divisible_tri_number(limit):
    i = 1
    while True:
        tri_nb = (i * (i + 1)) / 2
        if i % 2 == 0:
            nb_div = nb_divisors(i/2) * nb_divisors(i+1)
        else:
            nb_div = nb_divisors(i) * nb_divisors((i + 1)/2)
        if nb_div > limit:
            return tri_nb
        i += 1


print highly_divisible_tri_number(500)
