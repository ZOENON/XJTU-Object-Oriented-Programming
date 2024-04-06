# 求n个数的最大公约数。其中：2<=n<50

# 输入：n个正整数，用空格隔开，在一行内输入。

# 输出：最大公约数和这n个数，分2行输出。
c=list(map(int,input().split()))
l=len(c)
a=c[0]
for i in range(l-1):
    b=c[i+1]
    while b != 0:
        a,b=b,a%b

# output=list(map(str,c))
# r=" ".join(output)

print(a)
print(*c)
#或者 print(a,'\n',r,sep="")
#语法格式：print(*objects, sep=' ', end='\n', file=sys.stdout)，此处step设置为空，是为了去掉输出之间的空格（不然print默认空格作为分割））
#用两个print的话a和r之间不需要加\n是因为print自带的end



