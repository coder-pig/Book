"""
Pipe管道类使用代码示例
"""
import multiprocessing as mp

def p_1(p):
    p.send("你好啊！")
    print("P1-收到信息：", p.recv())

def p_2(p):
    print("P2-收到信息：", p.recv())
    p.send("你也好啊！")


if __name__ == '__main__':
    pipe = mp.Pipe()
    p1 = mp.Process(target=p_1, args=(pipe[0],))
    p2 = mp.Process(target=p_2, args=(pipe[1],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()