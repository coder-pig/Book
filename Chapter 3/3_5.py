"""
逻辑运算符示例
"""
score = 70
# 逻辑与，两个表达式都成立，才执行
if score > 60 and score < 100:
    print('分数及格')


# 逻辑与，有一个表达式成立就执行
score = -10
if score < 0 or score > 100:
    print("分数值非法，不能小于0或者大于100")

# 逻辑非，逆转，表达式成立的话反而不执行
score = 100
if not score == 100:
    print("没有满分")
else:
    print("满分")
