"""
Lock指令锁使用代码示例
"""
import threading

file_name = "test.txt"
lock = threading.Lock()


# 定义一个写入文件的方法(加锁)
def write_to_file(msg):
    if lock.acquire():
        try:
            with open(file_name, "a+", encoding="utf-8") as f:
                f.write(msg + "\n")
        except OSError as reason:
            print(str(reason))
        finally:
            lock.release()


class MyThread(threading.Thread):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def run(self):
        write_to_file(self.name + "~" + self.msg)


if __name__ == '__main__':
    for i in range(1, 101):
        t = MyThread(str(i)).start()
