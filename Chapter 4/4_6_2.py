"""
字典创建
"""
# 直接通过大括号进行创建
dict_1 = {}  # 定义一个空字典
dict_2 = {'a': 1, 'b': 2, 3: "c"}  # 定义一个普通字典
dict_3 = dict_2.copy()  # 浅复制一个字典

# 通过dict函数创建字典
dict_4 = dict(a=1, b=2, c=3)
dict_5 = dict(zip(['a','b','c'],(1,2,3)))
dict_6 = dict([('a',1),('b',2),('c',3)])

# 通过fromkeys创建并返回新的字典，有两个参数，键和键对应的值
# 值可以不提供，默认None，不过有个输出结果要注意一下！！！
dict_7 = {}.fromkeys(['a','b','c'],[1,2,3])

# 输出字典：
print('dict_1：%s' % dict_1)
print('dict_2：%s' % dict_2)
print('dict_3：%s' % dict_3)
print('dict_4：%s' % dict_4)
print('dict_5：%s' % dict_5)
print('dict_6：%s' % dict_6)
print('dict_7：%s' % dict_7)
