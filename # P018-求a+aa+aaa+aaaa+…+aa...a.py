c=list(map(int,input().split()))
a=c[0]
b=c[1]
r=''
s=0
for i in range(b):
    r=r+str(a)+'+'
    s=s+a
    a=a*10+c[0]

print(r[0:-1]+'='+str(s))#这里用[]输出从第一位到倒数第二位，去掉了加号


#当然也可以初始化r=str(a)然后循环内r=r+'+'+str(a)，这样这里就可以直接输出r了

#关于[]的使用问题和注意事项，这个网址的内容讲得还挺全面的
#https://www.jb51.net/python/288597rjt.htm
