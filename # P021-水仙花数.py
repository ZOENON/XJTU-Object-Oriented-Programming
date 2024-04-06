# “水仙花数”是指一个三位正整数，其各位数字的立方和刚好等于该数本身，如：153＝1^3＋5^3＋3^3 

#（其中^表示乘方，5^3表示5的3次方），则153是一个“水仙花数”。

# 输入n, m，100<=n,m<1000, 求出[n,m]之间的水仙花数。若该区间没有水仙花数，输出-1.

# 输入：n,m，用空格隔开。

# 输出：若干水仙花数，用空格隔开（最后一位输出后面无空格）。

'''
这里是第一个版本
s=list(map(int,input().split()))
a=int(s[0])
b=int(s[1])
output=''
for i in range(a-1,b):
    d=pow(i//100,3)
    e=pow(i//10-(i//100)*10,3)
    f=pow(i%10,3)
    if i==d+e+f:
        output=output+str(i)+' '
if output=='':
    print('-1')
else:
    print(output[:-1])

'''
a,b=map(int,input().split())
c=[]
for i in range(a-1,b):
    d,e,f=map(int,str(i))#这里用的是数据解包的方法
    if i==d**3+e**3+f**3:
    output=output+str(i)+' '
              
if c==[]:
    print('-1')
else:
    print(*c)
