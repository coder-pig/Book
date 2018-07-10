"""
定义类与示例
"""


class Bird:
    """
    鸟类
    """
    kind = '动物'
    name = "鸟"

    def __init__(self, name, wings):
        self.name = name
        self.wings = wings

    def can_fly(self, can):
        print("%s有 %s 的翅膀，%s飞翔" % (self.name, self.wings, '能' if can else '不能'))


if __name__ == '__main__':
    eagle = Bird("老鹰", "长而宽阔")
    duck = Bird("鸭子", "较短")
    eagle.can_fly(True)
    duck.can_fly(False)

    print("类访问类变量：%s" % Bird.kind)
    print("类访问变类量：%s" % Bird.name)
    print("实例访问类变量：%s" % eagle.kind)
    print("实例访问同名变量：%s" % duck.name)
