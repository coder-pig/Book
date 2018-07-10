"""
访问控制代码示例
"""


class People:
    sex = 1  # 类属性
    __skill = "敲代码"  # 私有类属性，只能类内部访问，外部无法访问
    _hello = 1

    def speak(self):
        print("我是一个人，技能是：%s" % self.__skill, end='\t')


people = People()
people.speak()
people.sex = -1
print("性别：" + ("男" if people.sex == 1 else "女"))
print("访问私有属性：%s" % people._People__skill)
