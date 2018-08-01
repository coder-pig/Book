"""
利用itchat定时发送信息
"""
import itchat
from apscheduler.schedulers.blocking import BlockingScheduler
import time


# 发送信息
def send_msg():
    user_info = itchat.search_friends(name='培杰')
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        itchat.send_msg('生日快乐哦！', toUserName=user_name)


def after_login():
    sched.add_job(send_msg, 'cron', year=2018, month=7, day=28, hour=16, minute=5, second=30)
    sched.start()


def after_logout():
    sched.shutdown()


if __name__ == '__main__':
    sched = BlockingScheduler()
    itchat.auto_login(loginCallback=after_login, exitCallback=after_login)
    itchat.run()
