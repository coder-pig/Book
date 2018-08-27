# 1.最简单的，try捕获了任何异常，直接丢给except后的代码块处理：
try:
    result = 1 / 0
except:
    print("捕获到异常了!")
