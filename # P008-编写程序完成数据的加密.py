n=input()
n=list(map(int,n))
for i in range(4):
    n[i]=(n[i]+5)%10
for i in n[::-1]:
    print(i,end='')
