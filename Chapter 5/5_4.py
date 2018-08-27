"""
循环控制break 使用示例
"""
import random

# 打印出1-100里所有的奇数
# print("输出1-100之间所有的奇数：")
# for i in range(1, 101):
#     if i % 2 == 0:
#         if i % 20 == 0: print()
#         continue
#     else:
#         print(i, end='\t')

# 随机生成20个成绩，获取第一个不合格的成绩
score_list = []
pos = 1
while pos < 21:
    score_list.append(random.randint(0, 100))
    pos += 1
print("随机生成的成绩列表：\n%s" % score_list)
for score in score_list:
    if score < 60:
        print("第一个不及格的成绩是：%s" % score)
        break
