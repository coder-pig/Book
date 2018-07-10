"""
类动态绑定属性与函数示例
"""


class A:
    def __init__(self, id_):
        self.id_ = id_


# 定义一个用于动态绑定的函数
def set_name(self, name):
    print("调用了动态绑定的函数")
    self.name = name


if __name__ == '__main__':
    # 动态绑定一个属性
    A.kind = "人类"
    # 动态绑定一个函数
    A.set_name = set_name
    a = A(1)
    # 类访问动态绑定的属性
    print(A.kind)
    # 实例访问动态绑定的属性
    print(a.kind)
    # 类访问动态绑定的函数
    A.set_name(a,'123')
    # 实例访问动态绑定的函数
    a.set_name('321')
