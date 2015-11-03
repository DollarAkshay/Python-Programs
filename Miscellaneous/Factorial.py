def fact(i):
	if i==0:
		return 1
	return fact(i-1)*i

for i in range(7):
	print fact(i)