"""
条件判断使用示例
"""
# 单分支(只有一个if)，如果代码块只有一条语句，可以和if语句写到一行
name = 'CoderPig'
if name == 'CoderPig': print("你是CoderPig")

# 双分支(if-else)
sex = "男"
if sex == '男':
    print("你是一个男性")
else:
    print("你是一个女性")

# 多分支(if-elif-else)
score = 78
if score == 100:
    print("满分！")
elif 90 <= score < 100:
    print("优秀！")
elif 80 <= score < 90:
    print("良好！")
elif 70 <= score < 80:
    print("中等！")
elif 60 < score < 70:
    print("差！")
else:
    print("不及格！")

a,b = 1, 2

c = a if a > b else b

print('c = %d' % c)

