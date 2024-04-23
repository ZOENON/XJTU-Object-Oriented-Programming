n=input()
for i in n:
    print(i+' ',end='')
    print(ord(i),end='')
    print(' '+chr(ord(i)+1))