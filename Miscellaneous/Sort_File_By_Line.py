f = open('Miscellaneous/Data/Graduation_Unordered.txt')
nameList = []
for line in f:
    line = line[3:-1]
    nameList.append(line)

nameList.sort()
f.close()
f = open('Miscellaneous/Data/Gradution_Ordered.txt', 'w')

for i, name in enumerate(nameList):
    number = str(i+1)
    if i<9:
        number = "0"+number
    if name=="Akshay L Aradhya":
        name = "*"+name+"*"
    f.write(number+" "+name+"\n")

f.close()