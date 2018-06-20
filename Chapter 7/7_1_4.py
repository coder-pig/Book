# 4.对多个异常统一处理
try:
    result = 1 / 0
    sum = 1 + '2'
except (TypeError, ZeroDivisionError) as reason:
    print(str(reason))