"""
列表的其他操作
"""
a_list = [1, 2.0, 'a', True]
b_list = [3, 2, 9, 4, 11]

# 可以使用+号组合列表，*号重复列表
print(a_list + a_list)
print(a_list * 2)

# 判断元素是否在列表中
print('a' in a_list)

# 获得列表长度
print('列表长度：%d' % len(a_list))

# 统计元素在列表中出现的次数,True的值也是1
print('列表中1出现的次数 %d' % a_list.count(1))

# 统计最大值，最小值，列表元素类型需要为数字
print('列表中的最大值 %d' % max(b_list))
print('列表中的最小值 %d' % min(b_list))

# 排序，本地排序(会修改值)，返回None，只能比较数字！默认从小到大，
# 从大到小可以用可选参数，括号里加上key = lambda x:-1*x
b_list.sort()
print('升序排列：%s' % b_list)
b_list.sort(key=lambda x: -1 * x)
print('降序排列：%s' % b_list)

# 列表元素反转，会修改列表，返回None
a_list.reverse()
print('反转后的列表：%s' % a_list)

