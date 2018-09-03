"""
itchat集成图灵API制作聊天机器人代码示例
"""
import itchat
import requests as rq


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    info = msg['Content'].encode('utf8')
    # 图灵API接口
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'
    # 接口请求数据
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": str(info)
            }
        },
        "userInfo": {
            "apiKey": "7e9377d76fc7ee9499f6dec8eed37bbb",
            "userId": "123"
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Host': 'openapi.tuling123.com',
        'User-Agent': 'Mozilla/5.0 (Wi`ndows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 '
                      'Safari/537.36 '
    }
    # 请求接口
    result = rq.post(api_url, headers=headers, json=data).json()
    # 提取text，发送给发信息的人
    itchat.send_msg(result['results'][0]['values']['text'], msg['FromUserName'])
    print()


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
