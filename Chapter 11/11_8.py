"""
定时器Timer使用代码示例
"""
import threading
import time


def skill_ready():
    print("菜肴制作完成！！！")


if __name__ == '__main__':
    t = threading.Timer(5, skill_ready)
    t.start()
    while threading.active_count() > 1:
        print("======菜肴制作中======")
        time.sleep(1)