"""
自定义Process类代码示例
"""
from multiprocessing import Process
import os


class MyProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.msg = name

    def run(self):
        print("子进程运行中：name = %s , pid = %d " % (self.msg, os.getpid()))

if __name__ == '__main__':
    print("父进程 %d" % os.getpid())
    p = MyProcess('测试')
    print("开始执行子进程~")
    p.start()
    p.join()
    print("子进程执行完毕！")

