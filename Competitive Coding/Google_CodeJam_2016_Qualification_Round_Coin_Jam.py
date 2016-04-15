
import math

temp = []
jamcoins = []
factors = []
pows = []

n = 16
j = 50

coin = '1'

for i in range(11):
    pows.append(i**(n-1))

def isPrime(n):
    lim = math.floor(pow(n, 0.5))
    for i in range(2,lim+1):
        if n%i==0:
            temp.append(i)
            return False
    return True

def isJamCoin(c):
    global temp
    for b in range(10,11):
        if isPrime(pows[b] + int(c,b)):
            temp = []
            return False
    factors.append(temp)
    temp = []
    return True

print("Case #1:")
while len(jamcoins)<j:
    if isJamCoin(coin):
        jamcoins.append(coin)
        print(coin, end=" ")
        for i in range(len(factors[len(factors)-1])):
            print( factors[len(factors)-1][i], end=" ")
        print("")
    coin = bin(int(coin, 2) + 2)[2:]
    
        
    

