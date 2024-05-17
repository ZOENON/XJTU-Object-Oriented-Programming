y, m = map(int, input().split(","))
big_month = [1, 3, 5, 7, 8, 10, 12]
small_month = [4, 6, 9, 11]
if m in big_month:
    print(31)
elif m in small_month:
    print(30)
elif (y & 4 == 0 and y & 100 != 0) or (y & 400 == 0):
    print(29)
else:
    print(28)
