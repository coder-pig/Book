"""
itchat查找用户代码示例
"""

import itchat
import time

if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的用户信息，返回自己的属性字典
    # result = itchat.search_friends()
    # print(result)

    # 根据姓名查找用户
    # result = itchat.search_friends(name='培杰')
    # print(result)

    # 根据微信号查找用户
    # result = itchat.search_friends(wechatAccount='zpj779878443')
    # print(result)

    # 根据userName查找用户
    result = itchat.search_friends(userName='@40b096c3036543e5b2d4de4fc22208ed')
    print(result)

