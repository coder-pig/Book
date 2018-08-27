"""
类装饰函数代码示例
"""


class class_func:
    def __init__(self, _func):
        self._func = _func

    def __call__(self, name):
        print("类装饰的方法名：", self._func.__name__, name)
        return self._func(name)


@class_func
def func(a):
    return a


if __name__ == '__main__':
    print(func('123'))
