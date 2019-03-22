# https://projecteuler.net/problem=2
# Even Fibonacci numbers


def fibonacciSumUntil(maxNumber):
    first = 1
    second = 2
    sum = 0
    while second < maxNumber:
        if second % 2 == 0:
            sum += second
        copyOfSecond = second
        second = first + second
        first = copyOfSecond
    return sum

print fibonacciSumUntil(4000000)
