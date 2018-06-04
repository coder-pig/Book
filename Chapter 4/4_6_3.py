"""
访问字典元素示例
"""
dict_1 = {'a': 1, 'b': 2, 3: "c"}

# 通过键查询对应的值，如果没有这个键会报错TypeError
print(dict_1['b'])
# 通过get()方法查询键对应的值，没有的话会返回None
print(dict_1.get('d'))
# 和get()类似，如果找不到键的话会自动添加键，并赋值None
print(dict_1.setdefault('d'))
print(dict_1)
# 判断字典中是否有某个键
print('d' in dict_1)
print(dict_1.__contains__('d'))
# 获得字典里所有的键
print(dict_1.keys())
# 获得字典里所有的值
print(dict_1.values())
# 获得字典里所有的键值对
print(dict_1.items())

