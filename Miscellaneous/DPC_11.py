l = 28124
ds=list(range(0,-l,-1))
for i in range(1,l):
    for j in range(0,l,i): ds[j]+=i
print (l*(l-1)/2-sum(set([(i+j)for i in range(1,l)for j in range(i,l)if ds[i]>i and ds[j]>j and (i+j)<l])))

