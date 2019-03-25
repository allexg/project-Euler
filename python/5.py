# https://projecteuler.net/problem=5
# Smallest multiple


def greatest_common_divisor(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def smallest_multiple(a, b):
    return (a * b) / greatest_common_divisor(a, b)


# lcm (least common multiple) of a, b, c = lcm(a, lcm(b, c))
def smallest_multiple_for_list(numbers):
    smallest_mul = smallest_multiple(numbers[0], numbers[1])
    if len(numbers) > 2:
        for i in range(2, len(numbers)):
            smallest_mul = smallest_multiple(smallest_mul, numbers[i])
    return smallest_mul


# smallest multiple for numbers 11 to 20 is the same as for 1 to 20
numbers = range(11, 21)
print smallest_multiple_for_list(numbers)
