"""
多继承代码示例
"""


class A:
    def show_A(self):
        print('父类A')


class B:
    def show_B(self):
        print('父类B')


# 定义一个子类，继承A和B类
class C(A, B):
    def show_C(self):
        print('子类C')

if __name__ == '__main__':
    c = C()
    c.show_A()
    c.show_B()
    c.show_C()
    print(C.__mro__)
