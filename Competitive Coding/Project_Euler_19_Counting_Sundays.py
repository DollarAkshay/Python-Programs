
def dayofweek(y, m, d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m < 3:
        y -= 1
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7


count = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if dayofweek(y, m, 1) == 0:
            count += 1

print(count)
