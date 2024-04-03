# 编程判断任意一个正整数各位数字之和是奇数还是偶数。
# 如果和是奇数输出1，偶数输出0。

c=list(map(int,input()))
#map函数的基本语法为map(function, iterable, ...)，map() 函数将 function 应用于 iterable 中的每个元素并返回迭代后的结果
print(sum(c)%2)#sum函数可以直接求list里面数据的和
