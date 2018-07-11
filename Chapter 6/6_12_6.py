"""
类装饰类代码示例
"""


class class_class:
    def __init__(self, _cls):
        self._cls = _cls

    def __call__(self, name):
        print("类装饰的类的类名：", self._cls.__name__, name)
        return self._cls(name)


@class_class
class A:
    def __init__(self, a):
        self.a = a

    def show(self):
        print('self.a = ', self.a)


if __name__ == '__main__':
    a = A('123')
    a.show()
