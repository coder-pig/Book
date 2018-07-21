import threading
import queue
import time
import random

work_queue = queue.Queue()


# 任务模拟
def working():
    global work_queue
    while not work_queue.empty():
        data = work_queue.get()
        time.sleep(random.randrange(1, 2))
        print("执行" + data)
        work_queue.task_done()


# 工作线程
class WorkThread(threading.Thread):
    def __init__(self, t_name, func):
        self.func = func
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        self.func()


if __name__ == '__main__':
    work_list = []
    for i in range(1, 21):
        work_list.append("任务 %d" % i)
    # 模拟把需要执行的任务放到队列中
    for i in work_list:
        work_queue.put(i)
    # 初始化一个线程列表
    threads = []
    for i in range(0, len(work_list)):
        t = WorkThread(t_name="线程" + str(i), func=working)
        t.daemon = True
        t.start()
        threads.append(t)
    work_queue.join()
    for t in threads:
        t.join()
    print("所有任务执行完毕")
