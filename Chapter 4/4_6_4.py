"""
修改字典示例
"""
dict_1 = {'a': True, 'b': 2, 3: "c"}
dict_1['b'] = 'HaHa'
print(dict_1)
# 把别的字典里的键值对更新到字典里
dict_1.update({'d':'Pig', 'e':'1'})
print(dict_1)
