"""
函数装饰类代码示例
"""


def func_class(cls):
    def decorator(name):
        print("函数修饰的类：", cls.__name__, name)
        return cls(name)

    return decorator


@func_class
class A:
    def __init__(self, n):
        self.n = n

    def show(self):
        print("a = " + self.n)


a = A('123')
a.show()
