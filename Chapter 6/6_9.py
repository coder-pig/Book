"""
最简单的生成器使用例子
"""


def func(n):
    yield n * n


if __name__ == '__main__':
    print(func(10))
    print(next(func(10)))
    for i in func(10):
        print(i)