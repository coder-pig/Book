"""
itchat监听信息并响应代码示例
"""
import itchat


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    if msg['Content'] == u'你好':
        itchat.send_msg(msg['User']['NickName'] + "你好啊！", msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
