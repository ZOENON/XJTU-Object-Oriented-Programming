def ispalindrome(n):
    if (n//1000)==(n%10) and (n//10%10)==(n//100%10):
        return True
    else:
        return False
op=[]
n=input()
for i in range(1000,int(n)+1):
    if ispalindrome(i):
        op.append(str(i))
op=" ".join(op)
print(op)



