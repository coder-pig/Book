"""
time 与 datetime 模块使用示例
"""

import time, datetime

# 获取当前时间
moment = time.localtime()
print("年：%s" % moment[0])
print("月：%s" % moment[1])
print("日：%s" % moment[2])
print("时：%s" % moment[3])
print("分：%s" % moment[4])
print("秒：%s" % (moment[5] + 1))
print("周几：%s" % (moment[6] + 1))
print("一年第几天：%s" % moment[7])
print("是否为夏令时：%s" % moment[8])

# 格式化时间(这里要注意strftime和strptime是不一样的！！！)
moment1 = time.strftime('%Y-%m-%d %H:%M:%S')
moment2 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
moment3 = time.mktime(time.strptime(moment2, '%a %b %d %H:%M:%S %Y'))
print(moment1)
print(moment2)
print(moment3)

# 获得当前时间戳
print(time.time())

# 获得当前时间(时间数组，还需strftime格式化下)
print(datetime.datetime.now())

# 时间戳转换为时间
# 方法一：
moment4 = 1512184082
moment5 = time.localtime(moment4)  # 转换成时间数组
print(time.strftime('%Y-%m-%d %H:%M:%S', moment5))  # 格式化
# 方法二：
moment6 = datetime.datetime.utcfromtimestamp(moment4)
print(moment6)
moment7 = moment6.strftime('%a %b %d %H:%M:%S %Y')
print(moment7)

# 代码延迟执行
time.sleep(5)

