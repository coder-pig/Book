"""
多进程数据共享：Value和Array使用示例
"""
import multiprocessing as mp

def do_something(num, arr):
    num.value += 1
    for i in range(len(arr)):
        arr[i] = arr[i] * 2
if __name__ == '__main__':
    value = mp.Value('i', 1)
    array = mp.Array('i', range(5))
    print("刚开始的值：", value.value, array[:])

    # 创建进程1
    p1 = mp.Process(target=do_something, args=(value, array))
    p1.start()
    p1.join()
    print("进程1操作后的值：", value.value, array[:])

    # 创建进程2
    p2 = mp.Process(target=do_something, args=(value, array))
    p2.start()
    p2.join()
    print("进程2操作后的值：", value.value, array[:])