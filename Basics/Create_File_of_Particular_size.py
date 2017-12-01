
FILE_PATH = "C:\\Users\\akshay.aradhya\\Documents\\Miscellaneous\\"
filename = input("Enter file name : ")
size = int(input("Enter file Size in bytes : "))

print(filename, '|', size)

f = open(FILE_PATH + filename, "wb")
f.seek(size - 1)
f.write(b"\0")
f.close()
