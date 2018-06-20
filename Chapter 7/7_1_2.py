# 2.捕获特定类型：
try:
    result = 1 / 0
except ZeroDivisionError:
    print("捕获到除数为零的错误")