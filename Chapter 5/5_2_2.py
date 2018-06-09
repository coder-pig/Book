"""
for循环代码示例
"""
result = 0
for pos in range(1,101):
    result += pos
    continue
else:
    print("====== 输出1-100的求和结果 ====== \n%d" % result)