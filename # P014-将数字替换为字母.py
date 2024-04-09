a=input()
c=int(int(a)/2)
print(c,end=' ')
c=str(c)
n=ord('a')-ord('0')
result=''
for i in range(len(c)):
    b=chr(ord(c[i])+n)
    result+=b
print(result)