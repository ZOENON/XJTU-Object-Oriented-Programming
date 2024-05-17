def run(y):
    if (y%4==0 and y%100!=0) or (y%400==0):
        return True
    else:
        return False
y,n=map(int,input().split())
while not run(y):
    y+=1
for i in range(n-1):
    if run(y+4):
        y=y+4
    else:
        y=y+8
print(y)