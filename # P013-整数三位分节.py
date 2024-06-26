# 写出正整数的三位分节格式。如，当用户输入82668634时，程序应该输出82,668,634。
# 输入：正整数
# 输出：三位分解格式。
# 样例：
# 82668634
# 82,668,634

def format_number_with_commas(number):
    """
    将正整数格式化为三位分节格式。
    输入：正整数（number）
    输出：格式化后的字符串
    """
    # 将数字转换为字符串，并使用逗号进行三位分节
    formatted_number = f"{number:,}"
    return formatted_number
formatted_output = format_number_with_commas(int(input()))
print(formatted_output)
