n,m=map(int,input().split())
sum=0
for i in range(n,m+1):
    for j in range(i,m+1):
        for k in range(j,m+1):
            if k**2==j**2+i**2:
                sum=sum+1
print(sum)
