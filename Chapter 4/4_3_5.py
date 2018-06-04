"""
随机数使用示例
"""
import random

# 1.生成一个范围在0.0~1.0间的浮点数
print(random.random())

# 2.生成一个有上限和下限范围的浮点数
print(random.uniform(2, 3))

# 3.生成一个在某个范围内的随机整数
print(random.randint(1, 5))

# 4.随机返回某个序列里的一个元素
word_list = ['佩奇', '乔治', '苏西', '丹妮', '瑞贝卡']
print(random.choice(word_list))

# 5.把一个序列里所有元素随机打乱
random.shuffle(word_list)
print(word_list)

# 6 从指定的序列中，随机裁剪一定个数的元素，组成一个新的序列，不会影响原序列
print(random.sample(word_list, 3))
