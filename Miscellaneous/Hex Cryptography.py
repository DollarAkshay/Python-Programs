
a = int("000000e5", 16)
res = a^(a<<1)^(a<<7)


print(format( res, '08x'))
