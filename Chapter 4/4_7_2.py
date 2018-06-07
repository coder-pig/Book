"""
集合的基本操作示例
"""

# 1.集合创建
set_1 = set()  # 创建一个空集合
set_2 = {1, 2, 3, 4, 5, 1, 2}  # 普通方式创建集合，重复元素会被自动删除
set_3 = set('12345')    # 通过字符串构建，注意元素无序
set_4 = frozenset({1,2,3,4})    # 创建一个不可变集合
print("1.集合创建：")
print(set_1)
print(set_2)
print(set_3)
print(set_4)

# 2.判断元素是否在集合中
print("\n2.元素是否在集合中：")
print('集合中有6这个元素：%s' % (6 in set_1)) # 判断集合中是否有此元素
print('集合中没有7这个元素：%s' % (7 not in set_1)) # 判断集合中是否有此元素

# 3.集合增删元素
print("\n3.增删集合中的元素：")
set_1.add(6)
print("往集合中插入一个元素6后：%s" % set_1)
set_1.remove(6) # 如果删除的元素不存在会报错，建议先判断下是否存在运算再删除
print("往集合中删除一个元素6后：%s" % set_1)
set_1.discard(6)    # 删除集合中的一个元素，如果元素不存在，不执行任何操作
print("删除集合中的一个元素6后：%s" % set_1)
set_2.pop() # 无序随机删除并返回任意一个集合元素，集合为空会引发KeyError
print("随机弹出集合中的一个元素后：%s" % set_2)

# 4.集合遍历
print("\n4.遍历集合中的元素：\n set_2 =", end='')
for data in set_2:
    print(data, end='\t')

# 5.清空集合
set_2.clear()
print("\n\n5.清空集合中的元素 ：%s" % set_2)