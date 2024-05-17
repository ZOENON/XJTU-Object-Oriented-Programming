input_str=input()
input_str=input_str.upper()
dict={}
for i in range(0,26):
    dict[chr(ord('A')+i)]=input_str.count(chr(ord('A')+i))
#d.items()以列表的形式返回可遍历的元组数组
flag=0
for k,v in sorted(dict.items(), key=lambda item: item[1], reverse=True):
    if flag:
        print(' ',end='')
    else:
        flag=1
    print(f"{k}-{v}",end='')
