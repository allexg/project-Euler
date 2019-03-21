# https://projecteuler.net/problem=1
# Multiples of 3 and 5


def sumOf3or5Multiples(max):
    sum = 0
    for number in range(3, max):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum


# print sumOf3or5Multiples(10)
# print sumOf3or5Multiples(100)
print sumOf3or5Multiples(1000)
# print sumOf3or5Multiples(10000)
# print sumOf3or5Multiples(100000)
# print sumOf3or5Multiples(1000000)
# print sumOf3or5Multiples(10000000)
# print sumOf3or5Multiples(100000000)
