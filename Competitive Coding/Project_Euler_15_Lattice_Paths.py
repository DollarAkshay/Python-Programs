import time


def dfs(x, y, h, w):
    if x > w or y > h:
        return 0
    elif x == w and y == h:
        return 1
    else:
        return dfs(x + 1, y, h, w) + dfs(x, y + 1, h, w)


for h in range(1, 10):
    for w in range(1, 10):
        print("{:6d}".format(dfs(0, 0, h, w)), end=" ")
    print("")
