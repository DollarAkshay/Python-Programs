import urllib.request

file = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in file:
    print(line.decode('utf-8').strip())