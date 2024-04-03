# 输入2个整数，求：和，差，积，商
# 输入：2个整数（第二个数是非零整数）
# 输出：4个整数，依次为和、差、积和商，数据间用空格分隔。
a=list(map(float,input().split()))
b=int(a[0])
c=int(a[1])
print(b+c,b-c,b*c,b/c)
