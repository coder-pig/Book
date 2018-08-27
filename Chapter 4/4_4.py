"""
列表删除示例
"""
num_list = [0, 1, 2, 3, 4, 5]
num_list.remove(2)
print(num_list)  # 输出结果：[0, 1, 3, 4, 5]

del num_list[2]
print(num_list)  # 输出结果：[0, 1, 4, 5]

num_list.pop()
print(num_list)  # 输出结果：[0, 1, 4]

del num_list
print(num_list)  # 报错：NameError: name 'num_list' is not defined
