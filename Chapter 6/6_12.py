"""
多个装饰器装饰函数的执行顺序示例
"""


def func_a(func):
    def decorator():
        func()
        print("Call func_a")

    return decorator


def func_b(func):
    def decorator():
        func()
        print("Call func_b")

    return decorator


def func_c(func):
    def decorator():
        func()
        print("Call func_c")

    return decorator


@func_a
@func_b
@func_c
def func_t():
    pass


if __name__ == '__main__':
    func_t()
