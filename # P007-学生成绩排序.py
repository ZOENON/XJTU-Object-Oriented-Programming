n=int(input())
stu={}
for i in range(n):
    str=input().split()
    stu[str[0]]=[str[1],str[2],str[3],str[4],int(str[2])+int(str[3])+int(str[4])]
for key,value in sorted(stu.items(),key=lambda x:x[1][4]):
    print(key,value[0],value[1],value[2],value[3],value[4])
