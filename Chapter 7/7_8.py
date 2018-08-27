"""
自定义电话号码异常示例
"""
import re

# 自定义异常
class PhoneNumberException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


if __name__ == '__main__':
    phone_compile = re.compile(r'^(0|86|17951)?(13[0-9]|14[579]|15[0-35-9]|17[01678]|18[0-9])[0-9]{8}$')
    number = input("请输入一串手机号码：")
    if phone_compile.match(number) is not None:
        print("您输入的手机号码是：%s" % number)
    else:
        raise PhoneNumberException("非法的手机号码！")
