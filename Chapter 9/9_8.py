"""
单继承代码示例
"""


class Bird:
    def __init__(self, name):
        self.name = name

    def can_fly(self, can):
        self.can = can

    def __str__(self):
        return self.name + ("能够" if self.can == True else "不能够") + "飞翔。"


class Duck(Bird):
    # 子类扩展父类中的方法
    def set_color(self, color):
        self.color = color

    # 重写父类中里的方法
    def __str__(self):
        return self.color + "的" + self.name + ("能够" if self.can == True else "不能够") + "飞翔，" + "会游泳。"

if __name__ == '__main__':
    duck = Duck("小鸭子")
    duck.can_fly(False)
    duck.set_color("黄色")
    print(duck)
    # # 实例化一个父类对象
    bird = Bird('鸟')
    bird.can_swin()