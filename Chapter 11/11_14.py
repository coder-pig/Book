import multiprocessing as mp
import time


def func(msg):
    time.sleep(1)
    return mp.current_process().name + " : " + msg

if __name__ == '__main__':
    pool = mp.Pool()
    results = []
    for i in range(20):
        msg = "Do Something %d" % i
        results.append(pool.apply_async(func, (msg,)))

    pool.close()
    pool.join()
    for result in results:
        print(result.get())
    print("子进程执行任务完毕!")
