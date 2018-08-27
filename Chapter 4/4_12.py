"""
集合的其他操作示例
"""

set_1 = {'a', 'b', 'c', 'd', 'e', 'f'}
set_2 = set('cdefgh')
set_3 = set('ab')

# 进行数学集合运算
# 子集，集合为某个集合的一部分，使用操作符<，或issubset()进行判断
print('集合set_2是集合set_1的子集：%s' % (set_2 < set_1))
print('集合set_3是集合set_1的子集：%s' % (set_3.issubset(set_1)))

# 并集，两个集合所有元素构成的集合，使用操作符 | 或 union() 函数完成
print("集合set_1和集合set_2的并集：%s" % (set_1 | set_2))
print("集合set_1和集合set_2的并集：%s" % (set_1.union(set_2)))

# 交集，同时存在于两个集合中的元素构成的集合，使用操作符 & 或 intersection() 函数完成
print("集合set_1和集合set_2的交集：%s" % (set_1 & set_2))
print("集合set_1和集合set_2的交集：%s" % (set_1.intersection(set_2)))

# 差集，集合里有另一个集合里没有的元素构成的集合，使用操作符 - 或 difference() 函数完成
print("集合set_1和集合set_2的差集：%s" % (set_1 - set_2))
print("集合set_1和集合set_2的差集：%s" % (set_1.difference(set_2)))

# 对称差，只属于其中一个集合而不属于另一个集合的元素组成的集合
# 或者理解成全集除去交集部分元素后剩下的元素组成的集合
# 使用操作符 ^ 或 symmetric_difference() 函数完成
print("集合set_1和集合set_2的对称差：%s" % (set_1 ^ set_2))
print("集合set_1和集合set_2的对称差：%s" % (set_1.symmetric_difference(set_2)))

# 判断两个集合是否有交集
print("集合set_1和集合set_2存在交集：%s" % (set_1.isdisjoint(set_2)))

# 判断另一个集合是否包含这个集合
print("集合set_1中包含set_3这个集合：%s" % (set_1.issubset(set_3)))

# 判断一个集合是否包含另一个集合
print("集合set_2中包含set_3这个集合：%s" % (set_3.issuperset(set_2)))