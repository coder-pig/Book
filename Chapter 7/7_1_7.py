"""
raise显示抛出一个异常示例
"""
import re

# 注：这段正则你只需要知道是用来匹配电话号码的，正则在爬虫那一部分会详细讲解
phone_compile =re.compile(r'^(0|86|17951)?(13[0-9]|14[579]|15[0-35-9]|17[01678]|18[0-9])[0-9]{8}$')
number = input("请输入一串手机号码：")
if phone_compile.match(number) is not None:
    print("您输入的手机号码是：%s" % number)
else:
    raise ValueError
