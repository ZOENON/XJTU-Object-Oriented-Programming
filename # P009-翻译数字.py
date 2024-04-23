d={
    '1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
n=input()
flag=0
for i in n:
    if flag:
        print(" ",end='')
    else:
        flag=1
    print(d[i],end='')