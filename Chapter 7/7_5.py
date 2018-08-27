# 5.当没有检测到异常时才执行的代码块，可以用else
try:
    result = 4 / 2
except ZeroDivisionError as reason:
    print(str(reason))
else:
    print("没有发生异常，输出结果：%d" % result)
