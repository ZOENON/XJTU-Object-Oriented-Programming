def search_max(s):
    result=0
    for i in range(len(s)):
        count = 0
        for j in s[i:]:
            if j==s[i]:
                count+=1
            else:
                break
        if count > result:
            result = count
            word = s[i]
            index = i
    print(word,result,index)
s=input()
search_max(s)
