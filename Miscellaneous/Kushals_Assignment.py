import numpy as np


def calcD(x, y):
    global n, m
    return max(x / m - y / n, y / n - x / m)


def recursiveDP(x, y):
    global n, m
    if x > m or y > n:
        return 0
    if x == m and y == n:
        return 1
    elif number_of_paths[y][x] != 0:
        return number_of_paths[y][x]
    else:
        paths = 0
        paths += recursiveDP(x + 1, y)
        paths += recursiveDP(x, y + 1)
        number_of_paths[y][x] = paths
        return number_of_paths[y][x]


m = 11
n = 7

# Create 2D Matrix of size (n+1)x(m+1)
number_of_paths = [[0] * (m + 1) for i in range(n + 1)]
D = [[0] * (m + 1) for i in range(n + 1)]

recursiveDP(0, 0)

# Calculate D
for i in range(n + 1):
    for j in range(m + 1):
        D[i][j] = calcD(j, i)


# Convert to 1D flat list
values = []
freq = []
for i in range(n + 1):
    for j in range(m + 1):
        values.append(D[i][j])
        freq.append(number_of_paths[i][j])

# Calculate mean and standard deviation from a frequency distribution (weights)
# https://stackoverflow.com/questions/2413522/weighted-standard-deviation-in-numpy
mean = np.average(values, weights=freq)
std_dev = np.sqrt(np.average((values - mean)**2, weights=freq))

print("\nMean : ", mean)
print("Standard Deviation : ", std_dev)
