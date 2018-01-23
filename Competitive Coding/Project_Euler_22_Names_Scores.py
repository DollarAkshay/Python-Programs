import time

f = open("names.txt", "r")
name_list = [name.strip('"') for name in f.read().split(',')]
name_list = sorted(name_list)

total_score = 0
for i, name in enumerate(name_list):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    total_score += (i + 1) * score

print(total_score)
