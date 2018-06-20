"""
sys.exc_info函数获得异常信息示例
"""

import sys

try:
    result = 1 / 0
except:
    tuple_exception = sys.exc_info()

# 输出结果依次是：异常类，类示例，跟踪记录对象
for i in tuple_exception:
    print(i)
