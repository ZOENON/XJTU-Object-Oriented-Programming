num=input()
total=sum(int(num[i])*int(num[i]) for i in range(len(num)))
print(total)