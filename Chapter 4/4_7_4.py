"""
增删集合中的元素示例
"""
set_1 = {1, 2, 3, 4, 5}

set_1.add("6")  # 添加元素
print(set_1)

set_1.remove(2)  # 删除元素，如果删除的元素不存在会报错
print(set_1)
