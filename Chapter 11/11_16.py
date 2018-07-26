"""
Queue使用示例(单线程，多线程，多进程效率对比)
"""
import threading as td
import multiprocessing as mp
import time


def do_something(queue):
    result = 0
    for i in range(100000):
        result += i ** 2
    queue.put(result)


# 单线程
def normal():
    result = 0
    for _ in range(3):
        for i in range(100000):
            result += i ** 2
    print("单线程处理结果：", result)


# 多线程
def multi_threading():
    q = mp.Queue()
    t1 = td.Thread(target=do_something, args=(q,))
    t2 = td.Thread(target=do_something, args=(q,))
    t3 = td.Thread(target=do_something, args=(q,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("多线程处理结果：", (q.get() + q.get() + q.get()))


# 多进程
def multi_process():
    q = mp.Queue()
    p1 = mp.Process(target=do_something, args=(q,))
    p2 = mp.Process(target=do_something, args=(q,))
    p3 = mp.Process(target=do_something, args=(q,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("多进程处理结果：", (q.get() + q.get() + q.get()))


if __name__ == '__main__':
    start_time_1 = time.time()
    normal()
    start_time_2 = time.time()
    print("单线程处理耗时：", start_time_2 - start_time_1)
    multi_threading()
    start_time_3 = time.time()
    print("多线程处理耗时：", start_time_3 - start_time_2)
    multi_process()
    start_time_4 = time.time()
    print("多继承处理耗时：", start_time_4 - start_time_3)
