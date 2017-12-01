import math
import time


def getFactCount(n):
    if n == 0:
        return 0
    count = 0
    limit = int(math.sqrt(n))
    if limit * limit == n:
        # print("Perfect Square")
        count += 1

    for i in range(1, limit):
        if n % i == 0:
            count += 1
            # print(i, end=",")
    # print("")
    return count + math.floor(count / 2) * 2


max_fact = 1
max_n = 1
start_time = time.time()
for i in range(1, 50000):
    f = getFactCount(i * (i + 1) / 2)
    if f > max_fact:
        max_fact = f
        max_n = i * (i + 1) / 2
        print(max_n, "has the highest factors with", max_fact, "factors")
        if max_fact > 500:
            break

end_time = time.time()
print("Time Taken :", end_time - start_time, "sec")
