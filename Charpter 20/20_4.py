"""
itchat发送信息代码示例
"""
import itchat
import time


def after():
    user_info = itchat.search_friends(name='培杰')
    if len(user_info) > 0:
        # 拿到用户名
        user_name = user_info[0]['UserName']
        # 发送文字信息
        itchat.send_msg('培杰你好啊！', user_name)
        # 发送图片
        time.sleep(10)
        itchat.send_image('cat.jpg', user_name)
        # 发送文件
        time.sleep(10)
        itchat.send_file('19_2.py', user_name)
        # 发送视频
        time.sleep(10)
        itchat.send_video('sport.mp4', user_name)


if __name__ == '__main__':
    itchat.auto_login(loginCallback=after)
    itchat.run()
