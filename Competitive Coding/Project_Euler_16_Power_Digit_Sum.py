import math
import time


def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


print(sumDigits(2**1000))
