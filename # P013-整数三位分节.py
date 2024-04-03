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

"""
f-sting
**基本用法**:
```python
name = "Copilot"
message = f"Hello, {name}!"
print(message)  # 输出: Hello, Copilot!
```

**表达式**:
您可以在花括号中包含几乎任何有效的Python表达式：
```python
a = 5
b = 10
print(f"Five plus ten is {a + b} and not {2 * (a + b)}.")
# 输出: Five plus ten is 15 and not 30.
```

**格式规范**:
f-strings也支持格式规范，这允许您控制值的格式化方式。例如，您可以格式化数字，使其显示为特定数量的小数点位数：
```python
import math
print(f"The value of pi is approximately {math.pi:.3f}.")
# 输出: The value of pi is approximately 3.142.
```

在上面的例子中，`:.3f`是格式规范，它表示将数值格式化为带有三位小数的浮点数。

**大括号**:
如果您需要在字符串中包含大括号字符，您可以通过双写大括号来实现：
```python
print(f"{{73}} is the ASCII code of 'I'.")
# 输出: {73} is the ASCII code of 'I'.
```

**日期和时间**:
f-strings也可以与`datetime`模块一起使用，以格式化日期和时间：
```python
from datetime import datetime
today = datetime.now()
print(f"Today's date is {today:%B %d, %Y}.")
# 输出: Today's date is April 03, 2024.
```

在这个例子中，`:%B %d, %Y`是一个格式化代码，用于指定日期的显示格式。

总的来说，f-strings是一种强大且灵活的工具，可以帮助您以更清晰和高效的方式构建字符串。
"""
