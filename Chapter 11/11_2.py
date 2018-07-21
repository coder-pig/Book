"""
验证多线程快还是单线程快代码示例
"""
import threading
import time


def catch_fish():
    pass


def one_thread():
    start_time = time.time()
    for i in range(1, 1001):
        catch_fish()
    end_time = time.time()
    print("单线程测试 耗时 === %s" % str(end_time - start_time))


def muti_thread():
    start_time = time.time()
    for i in range(1, 1001):
        threading.Thread(target=catch_fish()).start()
    end_time = time.time()
    print("多线程测试 耗时 === %s" % str(end_time - start_time))


if __name__ == '__main__':
    # 单线程
    threading.Thread(one_thread()).start()
    # 多线程
    # muti_thread()
