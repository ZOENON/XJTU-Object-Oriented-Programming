n=list(map(int,input().split()))
a=[]
a.append(n.count(0))
a.append(n.count(1))
a.append(n.count(2))
a.append(n.count(3))
a.append(n.count(4))
flag=0
for i in a:
    if flag:
        print(' ',end='')
    else:
        flag=1
    print(i,end='')