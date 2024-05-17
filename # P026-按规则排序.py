n=map(int,input().split())
n=sorted(n)
s=len(n)
print(n[0],end=' ')
for i in range(int((s+1)/2-2)):
    print('0',end=' ')
print(n[-1],end=' ')
for i in range(int((s+1)/2-2)):
    print('0',end=' ')
print(n[int((s+1)/2)-1])
