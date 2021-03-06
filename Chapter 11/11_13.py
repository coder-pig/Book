"""
线程池使用代码示例
"""
import multiprocessing as mp
import time


def func(msg):
    time.sleep(1)
    print(mp.current_process().name + " : " + msg)


if __name__ == '__main__':
    pool = mp.Pool()
    for i in range(20):
        msg = "Do Something %d" % (i)
        pool.apply_async(func, (msg,))
    pool.close()
    pool.join()
    print("子进程执行任务完毕!")
