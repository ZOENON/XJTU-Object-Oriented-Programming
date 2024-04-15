# 去掉一个字符串中除头部和尾部空格外的所有空格。

# 样例：

#    abc  de

#    abcde
input_str = input()
n = 0
m = 0
# 找到第一个非空格字符的位置
for i in range(len(input_str)):
    if input_str[i] != " ":
        n = i
        break
# 找到最后一个非空格字符的位置
for i in range(len(input_str)):
    if input_str[-(i+1)] != " ":
        m = i
        break
# 去掉中间的空格
new_str = input_str.replace(" ", "")
print(" " * n + new_str + " " * m)
