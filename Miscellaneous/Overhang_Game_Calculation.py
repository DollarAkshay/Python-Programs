import time

start = time.time()
blocks = [0]
tick_length = 0.5
sum = 0
for i in range(1, 100000000):
    sum += 1 / (2 * i)
    if sum >= len(blocks) * tick_length:
        blocks.append(i)
        print("For {}th block sum = {}".format(i, sum))

print("Time taken : {}".format(time.time() - start))
print(blocks)
