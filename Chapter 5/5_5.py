"""
循环嵌套打印九九乘法表示例
"""
print("输出九九乘法表：")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d * %d = %d' % (i, j, i * j), end='\t')
        j += 1
    print()
    i += 1
