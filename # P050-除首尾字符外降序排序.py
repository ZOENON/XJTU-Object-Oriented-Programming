def str_sort(str):
    s_list=list(str)
    s_middle=sorted(s_list[1:-1:],reverse=True)
    print(str[0]+"".join(s_middle)+str[-1])
input_str=input()
str_sort(input_str)
