"""
itchat登录退出回调示例
"""
import itchat
import time


def after_login():
    print("登录后调用")


def after_logout():
    print("退出后调用")


if __name__ == '__main__':
    itchat.auto_login(loginCallback=after_login, exitCallback=after_logout)
    time.sleep(5)
    itchat.logout()
