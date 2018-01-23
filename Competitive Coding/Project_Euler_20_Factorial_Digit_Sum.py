import math
import time


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


print(sumDigits(fact(100)))
