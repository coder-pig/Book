"""
类实例动态绑定属性与函数示例
"""
from types import MethodType


class B:
    def __init__(self, id_):
        self.id_ = id_


# 定义一个用于动态绑定的函数
def set_name(self, name):
    print("调用了动态绑定的函数")
    self.name = name


if __name__ == '__main__':
    b_1 = B('1')
    # 动态为实例1绑定一个属性
    b_1.kind = "人类"
    # 动态为实例1绑定一个函数
    b_1.set_name = MethodType(set_name, b_1)
    # 实例1设置动态绑定的属性与函数
    print(b_1.kind)
    b_1.set_name('123')

    # 另一个类实例调用动态绑定的属性
    b_2 = B('2')
    print(b_2.kind)
