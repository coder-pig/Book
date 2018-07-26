"""
抓取我主良缘妹子交友信息做数据分析
"""

import requests as rq
import pandas as pd
import time
import random
import os

# 结果写入文件
result_save_file = 'wzly.csv'

# Ajax加载url
ajax_url = "http://www.lovewzly.com/api/user/pc/list/search?"

# 模拟请求头
ajax_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'www.lovewzly.com',
    'Referer': 'http://www.lovewzly.com/jiaoyou.html',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 '
                  'Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# post请求参数
form_data = {'gender': '2', 'marry': '1', 'page': '1'}

# csv表头
csv_headers = [
    '昵称', '用户id', '头像', '身高', '学历', '省份',
    '城市', '出生年份', '性别', '交友宣言'
]

height_interval = ['140', '150', '160', '170', '180']  # 身高范围
edu_interval = ['本科', '大专', '高中', '中专', '初中', '硕士', '博士', '院士']  # 学历范围
age_interval = [
    ('18-30', 8000), ('26-30', 8000), ('31-40', 8000),
    ('41-50', 8000), ('50以上', 8000),
] # 年龄范围


# 获取每页交友信息
def fetch_data(page):
    while True:
        try:
            form_data['page'] = page
            print("抓取第：" + str(page) + "页!")
            resp = rq.get(url=ajax_url, params=form_data, headers=ajax_headers)
            if resp.status_code == 200:
                data_json = resp.json()['data']['list']
                if len(data_json) > 0:
                    data_list = []
                    for data in data_json:
                        data_list.append((
                            data['username'], data['userid'], data['avatar'],
                            data['height'], data['education'], data['province'],
                            data['city'], data['birthdayyear'], data['gender'], data['monolog']))
                    result = pd.DataFrame(data_list)
                    if page == 1:
                        result.to_csv(result_save_file, header=csv_headers, index=False, mode='a+', encoding='utf-8')
                    else:
                        result.to_csv(result_save_file, header=False, index=False, mode='a+', encoding='utf-8')
            return None
        except Exception as e:
            print(e)


if __name__ == '__main__':
    if not os.path.exists(result_save_file):
        for i in range(1, 718):
            time.sleep(random.randint(2, 10))
            fetch_data(i)
