"""
字典遍历示例
"""
dict_1 = {'a': True, 'b': 2, 3: "c"}
# 方法一
for d in dict_1:
    print("%s:%s，" % (d, dict_1.get(d)),end='')
print()
# 方法二
for (k, v) in dict_1.items():
    print("%s:%s，" % (k, v),end='')