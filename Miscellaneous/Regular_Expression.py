import re

sum = 0
hand = open('data.txt')
for line in hand:
    a = re.findall('[0-9]+', line)
    for x in a:
        sum+=int(x)

print (sum)
