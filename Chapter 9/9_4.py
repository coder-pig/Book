"""
静态函数示例
"""
class C:
    @staticmethod
    def fun_c():
        print("Call fun_c()")

if __name__ == '__main__':
    C.fun_c()
    c = C()
    c.fun_c()