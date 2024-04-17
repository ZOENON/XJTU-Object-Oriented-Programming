str,n=input().split()
n=int(n)
op=''
for i in str:
    if ord('a')<=ord(i)<=ord("z"):
        op=op+chr((ord(i)+n-ord('a'))%26+ord('a'))
    else:
        op = op + chr((ord(i) + n-ord('A')) % 26 + ord('A'))
print(op)


