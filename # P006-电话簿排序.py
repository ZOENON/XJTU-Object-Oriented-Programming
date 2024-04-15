# 编写一个程序，读入n个用户姓名和电话号码，按姓名的字典顺序排列后，

# 输出用户的姓名和电话号码，n从键盘输入。
n=int(input())
# 创建一个空字典
dhb={}
# 循环输入n个用户姓名和电话号码
for i in range(n):
    str=input().split()
    dhb[str[0]]=str[1]
# 按姓名的字典顺序排列
for i in sorted(dhb.keys()):
    print(i,dhb[i])


