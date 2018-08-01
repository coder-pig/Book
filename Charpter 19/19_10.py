import itchat
from itchat.content import *
import os
import time
import re
import shutil
from apscheduler.schedulers.blocking import BlockingScheduler

# 文件临时存储页
rec_tmp_dir = os.path.join(os.getcwd(), 'tmp/')

# 存储数据的字典
rec_msg_dict = {}

# 过滤撤回信息的正则
revoke_msg_compile = re.compile(r'\<\!\[CDATA\[.*撤回了一条消息\]\]\>')

# 提取MsgId的正则
extract_msgid_compile = re.compile(r'\<msgid\>(.*?)\<\/msgid\>')


# 好友信息监听
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True)
def handle_friend_msg(msg):
    msg_id = msg['MsgId']
    msg_from_user = msg['User']['NickName']
    msg_content = ''
    # 收到信息的时间
    msg_create_time = msg['CreateTime']
    msg_type = msg['Type']

    if msg['Type'] == 'Text':
        msg_content = msg['Content']
    elif msg['Type'] == 'Picture' \
            or msg['Type'] == 'Recording' \
            or msg['Type'] == 'Video' \
            or msg['Type'] == 'Attachment':
        msg_content = r"" + msg['FileName']
        msg['Text'](rec_tmp_dir + msg['FileName'])
    rec_msg_dict.update({
        msg_id: {
            'msg_from_user': msg_from_user,
            'msg_create_time': msg_create_time,
            'msg_type': msg_type,
            'msg_content': msg_content
        }
    })


# 群聊信息监听
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def information(msg):
    msg_id = msg['MsgId']
    msg_from_user = msg['ActualNickName']
    msg_content = ''
    # 收到信息的时间
    msg_create_time = msg['CreateTime']
    msg_type = msg['Type']

    if msg['Type'] == 'Text':
        msg_content = msg['Content']
    elif msg['Type'] == 'Picture' \
            or msg['Type'] == 'Recording' \
            or msg['Type'] == 'Video' \
            or msg['Type'] == 'Attachment':
        msg_content = r"" + msg['FileName']
        msg['Text'](rec_tmp_dir + msg['FileName'])
    rec_msg_dict.update({
        msg_id: {
            'msg_from_user': msg_from_user,
            'msg_create_time': msg_create_time,
            'msg_type': msg_type,
            'msg_content': msg_content
        }
    })


# 撤回信息监控
@itchat.msg_register([NOTE], isFriendChat=True, isGroupChat=True)
def revoke_msg(msg):
    if revoke_msg_compile.search(msg['Content']) is not None:
        old_msg_id = extract_msgid_compile.search(msg['Content']).group(1)
        old_msg = rec_msg_dict.get(old_msg_id, {})
        # 先发送一条文字信息
        itchat.send_msg(str(old_msg.get('msg_from_user') + "撤回了一条信息："
                            + old_msg.get('msg_content')), toUserName="filehelper")
        # 判断msg_content是否存在，不存在说明是文字，就无需进行下一步
        if os.path.exists(os.path.join(rec_tmp_dir, old_msg.get('msg_content'))):
            # 判断聊天信息类型是否为图片，是调用发送图片的方法
            if old_msg.get('msg_type') == 'Picture':
                itchat.send_image(os.path.join(rec_tmp_dir, old_msg.get('msg_content')),
                                  toUserName="filehelper")
            # 判断聊天信息类型是否为视频，是调用发送视频的方法
            elif old_msg.get('msg_type') == 'Video':
                itchat.send_video(os.path.join(rec_tmp_dir, old_msg.get('msg_content')),
                                  toUserName="filehelper")
            # 判断聊天信息类型是否为附件或录音，是调用发送视频的方法
            elif old_msg.get('msg_type') == 'Attachment' \
                    or old_msg.get('msg_type') == 'Recording':
                itchat.send_file(os.path.join(rec_tmp_dir, old_msg.get('msg_content')),
                                 toUserName="filehelper")


# 每隔五种分钟执行一次清理任务
def clear_cache():
    # 当前时间
    cur_time = time.time()
    # 遍历字典，如果有创建时间超过2分钟(120s)的记录，删除，非文本的话，连文件也删除掉
    for key in list(rec_msg_dict.keys()):
        if int(cur_time) - int(rec_msg_dict.get(key).get('msg_create_time')) > 120:
            if not rec_msg_dict.get(key).get('msg_type') == 'Text':
                file_path = os.path.join(rec_tmp_dir, rec_msg_dict.get(key).get('msg_content'))
                print(file_path)
                if os.path.exists(file_path):
                    os.remove(file_path)
            rec_msg_dict.pop(key)


# 开始轮询任务
def start_schedule():
    sched.add_job(clear_cache, 'interval', minutes=2)
    sched.start()


# 退出停止所有任务并清空缓存文件夹
def after_logout():
    sched.shutdown()
    shutil.rmtree(rec_tmp_dir)


if __name__ == '__main__':
    sched = BlockingScheduler()
    if not os.path.exists(rec_tmp_dir):
        os.mkdir(rec_tmp_dir)
    itchat.auto_login(exitCallback=after_logout)
    itchat.run(blockThread=False)
    start_schedule()