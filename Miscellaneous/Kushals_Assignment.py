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

# Create a 2D Matrix of size (n+1)x(m+1)
number_of_paths = [[0] * (m + 1) for i in range(n + 1)]
D = [[0] * (m + 1) for i in range(n + 1)]

recursiveDP(0, 0)

# Calculate D
for i in range(n + 1):
    for j in range(m + 1):
        D[i][j] = calcD(j, i)

print("Number of Paths : ")
# Print the Matrix
for i in range(n + 1):
    for j in range(m + 1):
        print("{:6d} ".format(number_of_paths[i][j]), end="")
    print("")

print("\n\nD at x,y : ")
# Print the D Matrix
for i in range(n + 1):
    for j in range(m + 1):
        print("{:6f} ".format(D[i][j]), end="")
    print("")


# find mean(D[i][j] * number_of_paths[i][j])
val_sum = 0
for i in range(n + 1):
    for j in range(m + 1):
        val_sum += D[i][j] * number_of_paths[i][j]

print("\n\nMean of D : ")
print(val_sum / ((m + 1) * (n + 1)))
