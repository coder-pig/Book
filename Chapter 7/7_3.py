# 3.针对不同的异常设置多个except
try:
    sum = 1 + '2'
    result = 1 / 0
except TypeError as reason:
    print("类型出错：" + str(reason))
except ZeroDivisionError as reason:
    print("除数为0：" + str(reason))