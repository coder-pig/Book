"""
Ajax动态加载数据应对策略例子：爬取花瓣网某个画板的所有风景图
"""
import time
import random
import requests as r
import os
import re
import json

# 图片拼接url后，分别是前缀后缀
img_start_url = 'http://img.hb.aicdn.com/'
img_end = '_fw658'

# 获取pins的正则
boards_pattern = re.compile(r'pins":(.*)};')

# 修改pin_id的正则
max_pattern = re.compile(r'(?<=max=)\d*(?=&limit)')

# 图片id输出文件
pin_ids_file = 'pin_ids.txt'

# 图片输出路径
pic_download_dir = os.path.join(os.getcwd(), 'HuaBan/')

ajax_headers = {
    'Host': 'huaban.com',
    'Accept': 'application/json',
    'X-Request': 'JSON',
    'X-Requested-With': 'XMLHttpRequest'
}

# 往文件写入内容(追加)
def write_str_data(content, file_path, type="a+"):
    try:
        with open(file_path, type, encoding='utf-8') as f:
            f.write(content + "\n", )
    except OSError as reason:
        print(str(reason))

# 按行读取文件里的内容添加到列表中返回
def load_data(file_path):
    if os.path.exists(file_path):
        data_list = []
        with open(file_path, "r+", encoding='utf-8') as f:
            for ip in f:
                data_list.append(ip.replace("\n", ""))
        return data_list

# 获得borads页数据，提取key列表写入到文件里，并返回最后一个pid用于后续查询
def get_boards_index_data(url):
    print("请求：" + url)
    resp = r.get(url).text
    result = boards_pattern.search(resp)
    json_dict = json.loads(result.group(1))
    for item in json_dict:
        write_str_data(item['file']['key'], pin_ids_file)
    # 返回最后一个pin_id
    pin_id = json_dict[-1]['pin_id']
    return pin_id


# 模拟Ajax请求更多数据
def get_json_list(url):
    print("请求：" + url)
    resp = r.get(url, headers=ajax_headers)
    if resp is None:
        return None
    else:
        json_dict = json.loads(resp.text)
        pins = json_dict['board']['pins']
        if len(pins) == 0:
            return None
        else:
            for item in pins:
                write_str_data(item['file']['key'], pin_ids_file)
            return pins[-1]['pin_id']


# 下载图片的方法
def download_pic(key):
    url = img_start_url + key + img_end
    resp = r.get(url).content
    try:
        print("下载图片：" + url)
        pic_name = key + ".jpg"
        with open(pic_download_dir + pic_name, "wb+") as f:
            f.write(resp)
    except (OSError, r.HTTPError, r.ConnectionError, Exception) as reason:
        print(str(reason))


if __name__ == '__main__':
    if not os.path.exists(pic_download_dir):
        os.makedirs(pic_download_dir)
    if os.path.exists(pin_ids_file):
        os.remove(pin_ids_file)
    # 一个画板链接，可自行替换
    boards_url = 'http://huaban.com/boards/279523/'
    board_last_pin_id = get_boards_index_data(boards_url)
    board_json_url = boards_url + '?jl58nz3i&max=43131274&limit=20&wfl=1'
    while True:
        board_last_pin_id = get_json_list(max_pattern.sub(str(board_last_pin_id), board_json_url))
        if board_last_pin_id is None:
            break
    pic_url_list = load_data(pin_ids_file)
    for key in pic_url_list:
        download_pic(key)
    print("下载完成～")
