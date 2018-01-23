import math


def factorSum(n):
    if n <= 0:
        return 0
    lim = int(math.sqrt(n)) + 1
    res = 1
    for i in range(2, lim):
        if n % i == 0:
            res += i
            if i != int(math.sqrt(n)):
                res += n / i

    return int(res)


n = 10000
d = []
is_amicable = {}

for i in range(n):
    f_sum = factorSum(i)
    d.append(f_sum)

for i in range(n):
    f_sum = d[i]
    if f_sum < n and f_sum != i and d[f_sum] == i:
        is_amicable[f_sum] = 1
        is_amicable[i] = 1
        print(i, d[i], "|", f_sum, d[f_sum])


res = 0
for key in is_amicable:
    res += key

print(res)
