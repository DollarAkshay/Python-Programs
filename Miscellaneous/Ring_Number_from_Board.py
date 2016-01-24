
def ring(y, x, n):

    a = n//2
    b = (n-1)//2
    r = max(min(abs(x-6), abs(x-5)), min(abs(y-6), abs(y-5)));
    return min(5-r, r);

for i in range(12):
    for j in range(12):
        print( ring(i, j, 12), end=" ")
    print("")



    
    
