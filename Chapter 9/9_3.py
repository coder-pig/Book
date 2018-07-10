"""
成员函数代码示例
"""


class B:
    def fun_b(self):
        print("Call fun_b()")

if __name__ == '__main__':
    b = B()
    b.fun_b()
    B.fun_b(b)
