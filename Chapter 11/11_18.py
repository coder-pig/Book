"""
Manager类使用代码示例
"""
import multiprocessing as mp
import os
import time

def do_something(dt):
    dt[os.getpid()] = int(time.time())
    print(data_dict)

if __name__ == '__main__':
    manager = mp.Manager()
    data_dict = manager.dict()
    for i in range(3):
        p=mp.Process(target=do_something,args=(data_dict,))
        p.start()
        p.join()

