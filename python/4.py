# https://projecteuler.net/problem=4
# Largest palindrome product


def is_palindrome(n):
    return str(n) == str(n)[::-1]


# for nb_digits = 3, returns 999
def largest_number(nb_digits):
    return sum(10 ** exponent * 9 for exponent in range(nb_digits))


# nb_digits is for the 2 numbers that when multiplied, will result in palindrome
def largest_pal_from_prod_of_2(nb_digits):
    factor1 = largest_number(nb_digits)
    lowerLimit = largest_number(nb_digits - 1)

    while factor1 > lowerLimit:
        factor2 = factor1
        while factor2 > lowerLimit:
            prod = factor1 * factor2
            if is_palindrome(prod):
                return factor1, factor2, prod
            factor2 -= 1
        factor1 -= 1


print largest_pal_from_prod_of_2(3)
