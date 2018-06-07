"""
字符串的基本操作示例
"""

# 1.字符串创建
str_1 = "Hello Python!"
str_2 = str(123)

# 2.分片相关操作(和前面4.4.4列表操作一致)
print("str_1[3] = %s" % str_1[3])
print("str_1[2:] = %s" % str_1[2:])
print("str_1[2:5] = %s" % str_1[2:5])
print("str_1[2:10:2] = %s" % str_1[2:10:2])
print("str_1[0:8] + str_1[8:] = %s" % (str_1[0:8] + str_1[8:]))
print("str_1[6:] * 3 = %s" % (str_1[6:] * 3))
print("str_2的数据类型：%s" % type(str_2))

print(r'Python\n')
