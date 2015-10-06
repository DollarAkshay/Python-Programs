n,t = [int(i) for i in input().split()]

if n==1 and t==10:
    print("-1")
else:
    x = 10**(n-1);
    while True:
        if x%t==0:
            print(x)
            break
        x+=1
    
