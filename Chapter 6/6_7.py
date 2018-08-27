"""
迭代器使用示例
"""
import sys

a = [1, 2, 3, 4, 5]
it1 = iter(a)
print(type(it1))


# 直接遍历迭代器对象
for x in it1:
    print(x, end='\t')
else:
    print()

# 每调用一次next向后访问一个元素，超过元素会报StopIteration异常
it2 = iter(a)
print(next(it2), end='\t')
print(next(it2), end='\t')
print(next(it2), end='\t')
print(next(it2), end='\t')
print(next(it2), end='\t')
print()

# 带异常捕获方法
it3 = iter(a)
while True:
    try:
        print(next(it3), end='\t')
    except StopIteration:
        sys.exit()


