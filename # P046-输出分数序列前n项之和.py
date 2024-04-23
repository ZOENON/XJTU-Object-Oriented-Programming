def cal(a,b):
    return (a+b),a
n=int(input())
a=2
b=1
sum=0
for i in range(n):
    sum=sum+a/b
    a,b=cal(a,b)
print(f"{sum:.4f}")

