"""
itchat公众号相关使用代码示例
"""
import itchat


@itchat.msg_register(itchat.content.TEXT, isMpChat=True)
def reply_msg(msg):
    print("收到一条公众号信息：", msg['User']['NickName'], msg['Content'])


def login_after():
    mps = itchat.search_mps(name='CoderPig')
    if len(mps) > 0:
        print(mps)
        itchat.send_msg('人生苦短', toUserName=mps[0]['UserName'])


if __name__ == '__main__':
    itchat.auto_login(loginCallback=login_after)
    itchat.run()
