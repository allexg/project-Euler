# https://projecteuler.net/problem=9
# Special Pythagorean triplet


# parameter represents the sum of the triplets
# using the formula for generating pythagorean triplets: a = m^2 - n^2, b = 2mn, c = m^2 + n^2
def find_pythagorean_triplets(sum):
    for n in range(sum + 1):
        for m in range(n, sum + 1): # if inverse loops order (m first), we can also obtain the desired sum, but product will be negative
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            current_sum = a + b + c # 2m(m+n)
            if current_sum == sum:
                return a, b, c, a * b * c
            elif current_sum > sum:
                break
    raise Exception("Provided argument is not the sum of any pythagorean triplet")


print find_pythagorean_triplets(1000)
