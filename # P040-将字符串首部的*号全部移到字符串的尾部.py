n=input()
a=0
for i in n:
    if i=='*':
        a+=1
    else:
        break
print(n[a:]+"*"*a)