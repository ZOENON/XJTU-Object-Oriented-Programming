a=input()
t=''
for i in range(0,26):
    t=t+str(a.count(chr(ord('a')+i))+a.count(chr(ord('A')+i)))+","
print(t[:-1])

