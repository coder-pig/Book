"""
创建一个进程代码示例
"""
from multiprocessing import Process
import os


def show_msg(name):
    print("子进程运行中：name = %s , pid = %d " % (name, os.getpid()))


if __name__ == '__main__':
    print("父进程 %d" % os.getpid())
    p = Process(target=show_msg, args=('测试',))
    print("开始执行子进程~")
    p.start()
    p.join()
    print("子进程执行完毕！")
