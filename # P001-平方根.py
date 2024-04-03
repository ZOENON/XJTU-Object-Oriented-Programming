# 用户输入一个整数
x = int(input())

# 进入无限循环
while 1:
    # 如果输入的数小于等于0或大于1000
    if x <= 0 or x > 1000:
        # 输出0并要求用户重新输入
        print(0)
        x = int(input())
    else:
        # 如果输入的数在合法范围内，则导入math模块
        import math
        # 计算输入数的平方根并输出整数部分
        print(int(math.sqrt(x)))
        # 结束循环
        break
