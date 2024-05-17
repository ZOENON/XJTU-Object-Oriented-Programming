def join_output(s,t):
    str_join=s+t
    set_join=set(str_join)
    output=sorted(list(set_join))
    output="".join(output)
    print(output.upper())
str_input=input().split()
join_output(str_input[0],str_input[1])