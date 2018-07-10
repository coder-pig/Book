"""
类函数示例
"""


class A:
    @classmethod
    def fun_a(cls):
        print(type(cls), cls)


if __name__ == '__main__':
    A.fun_a()
    a = A()
    a.fun_a()
