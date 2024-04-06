# 输入一个字符串，删除串中的重复字符。

# 输入：要检查的字符串 例如：abacaeedabcdcd。

# 输出：  删除重复字符后的字符串。例如：abced。


'''
#1.比较传统的C语言思路
c=list(input())
l=len(c)
i=1
while i<l:
    for j in range(i):
        if c[i]==c[j]:
            c.pop(i)
            l-=1
            i-=1

            break
    i+=1

print(''.join(c))
'''

#以下方式已经经过检验

def remove_duplicates(input_str):
    # 使用集合来存储已经出现过的字符
    seen = set()
    # 用于存储删除重复字符后的结果
    result = []

    for char in input_str:
        if char not in seen:
            # 如果字符不在集合中，将其添加到集合和结果中
            seen.add(char)
            result.append(char)

    # 将结果列表转换为字符串并返回
    return ''.join(result)

# 测试示例
input_str = input()
output_str = remove_duplicates(input_str)
print(output_str) 
