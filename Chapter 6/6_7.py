"""
函数闭包代码示例
"""


def outer(a):
    b = 1

    def inner():
        print(a + b)

    return inner


if __name__ == '__main__':
    test_1 = outer(2)
    print(test_1.__closure__)
    print(test_1.__closure__[0].cell_contents)
    print(test_1.__closure__[1].cell_contents)