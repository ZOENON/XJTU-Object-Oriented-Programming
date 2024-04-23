def tonggou(n):
    if n**2%(10**len(str(n)))==n:
        ans.append(str(i))
ans=[]
n,m=map(int,input().split())
for i in range(n,m):
    tonggou(i)
print(' '.join(ans))

