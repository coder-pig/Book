"""
生成器实现斐波那契数列示例
"""


def func(n):
    a, b = 0, 1
    while n > 0:
        n -= 1
        yield b
        a, b = b, a + b


for i in func(10):
    print(i, end="\t")
