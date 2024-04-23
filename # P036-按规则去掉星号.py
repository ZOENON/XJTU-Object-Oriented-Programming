n=input()
a=0
b=0
for i in n:
    if i=='*':
        a+=1
    else:
        break
for i in n[:0:-1]:
    if i=='*':
        b+=1
    else:
        break
print(n[a:len(n)-b])
