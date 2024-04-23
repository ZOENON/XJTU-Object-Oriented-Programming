str,n=input().split()
n=int(n)
a=0
for i in str[:0:-1]:
    if i=="*":
        a+=1
    else:
        break
if a>n:
    print(str[:len(str)-(a-n)])
else:
    print(str)