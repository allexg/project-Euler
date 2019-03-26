# https://projecteuler.net/problem=6
# Sum square difference


print sum(i for i in range(101)) ** 2 - sum(i ** 2 for i in range(101))
