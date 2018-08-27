"""
利用dir函数查看所有的内置函数
"""
import sys

count = 1
methods = dir(sys.modules['builtins'])
for method in methods:
    if count % 5 == 0:
        print(method)
    else:
        print(method, end='\t')
    count += 1
