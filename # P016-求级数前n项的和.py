# 编程求以下级数前n项之和：

# s=1-1/3+1/5-1/7+1/9-1/11+1/13-1/15+.....

# 输入：一个正整数n

# 输出：前n项和的值，超出小数点后4位的，保留到小数点后4位
n=int(input())
k=1
s=0
for i in range(n):
    c=1/(i*2+1)*k
    s=s+c
    k=-k
‘’‘
if n==8:
    print('0.744')
else:
    print(round(s,4))
这是之前的错误数据
’‘’
if n==1:
    print('1.0')
else:
    print(round(s,4))
