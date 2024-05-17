def prime(n):
    for i in range(n-1,1,-1):
        if n%i==0:
            return False
            break
    return True
m,n=map(int,input().split())
result=0
for i in range(m,n-1):
    if prime(i):
        if prime(i+2):
            result+=1
print(result)