number = 0
s = 'CM'
mydict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

for i in range(len(s)):
    if i < len(s) - 1 and mydict[s[i]] < mydict[s[i + 1]]:
        number = number - mydict[s[i]]
    else:
        number = number + mydict[s[i]]

print(number)
