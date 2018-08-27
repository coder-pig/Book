"""
外部函数调用内部函数报错示例
"""


def fun_x():
    x = [10]
    y = 10

    def fun_y():
        x[0] += x[0]
        nonlocal y
        y *= y
        return x[0] * y
    return fun_y()


if __name__ == '__main__':
    print(fun_x())
