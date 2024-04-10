n=int(input())
i=2
l=[]
while n>1:
    if n%i==0:
        n=n/i
        l.append(str(i))
    else:
        i=i+1
li="*".join(l)
print("1*"+li)

