# 6.无论是否发生异常都会执行的一段代码块，比如io流关闭，
# 可以使用finally子句，如果发生异常先走except子句，后走finally子句。
try:
    result = 4 / 2
except ZeroDivisionError as reason:
    print(str(reason))
else:
    print("没有发生异常，输出结果：%d" % result)
finally:
    print("无论是否发生异常都会执行～")