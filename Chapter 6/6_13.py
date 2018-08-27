"""
函数装饰函数
"""


def func_func(func):
    def decorator(a, b):
        print("函数修饰的函数名：", func.__name__)
        result = func(a, b)
        return result

    return decorator


@func_func
def func_add(a, b):
    return a + b


if __name__ == '__main__':
    print(func_add(1, 2))
