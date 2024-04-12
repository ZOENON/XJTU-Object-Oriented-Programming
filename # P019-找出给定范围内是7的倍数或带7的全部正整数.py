n,m=map(int,input().split())
for i in range(n,m+1):
    if i%7==0:
        print(f"{i} is a multiple of 7")
    n=i
    while n>1:
        temp=n%10
        if temp==7:
            print(f"{i} contains 7")
            break
        n=n//10