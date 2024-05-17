def max_gewei(n):
    s=sorted(str(n),reverse=True)
    return s
n=int(input())
r=n*3
print(r,end=' ')
s=max_gewei(r)
for i in s:
    print(i,end='')
