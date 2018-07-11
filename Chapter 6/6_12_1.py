"""
装饰器代码示例
"""
import time


def 计时(配料="珍珠"):
    def decorator(func):
        def inner():
            print("加入配料：%s" % 配料 )
            start = time.time()
            func()
            end = time.time()
            print("耗时", end - start)
            return func
        return inner

    return decorator


@计时(配料='波霸')
def 波霸奶茶():
    time.sleep(1)
    print("制作一杯波霸奶茶")


@计时(配料='椰果')
def 四季奶绿():
    time.sleep(2)
    print("制作一杯四季奶绿")


if __name__ == '__main__':
    波霸奶茶()
    print()
    四季奶绿()
