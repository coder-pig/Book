"""
多线程写入同一个文件引起线程同步安全问题示例
"""
import threading

file_name = "test.txt"


# 定义一个写入文件的方法
def write_to_file(msg):
    try:
        with open(file_name, "a+", encoding="utf-8") as f:
            f.write(msg + "\n")
    except OSError as reason:
        print(str(reason))


class MyThread(threading.Thread):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def run(self):
        write_to_file(self.name + "~" + self.msg)


if __name__ == '__main__':
    for i in range(1, 21):
        t = MyThread(str(i)).start()
