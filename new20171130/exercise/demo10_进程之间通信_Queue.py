"""
需求：
    进程二：打印数据，
        从Queue获取数据并打印

    进程一：处理数据
        处理数据，并存入到Queue中
"""
from multiprocessing import *
import os
import time
import random


# 处理数据的任务：向队列中存入消息
def write_fn(q):
    print("我是处理数据的进程：%d" % os.getpid())
    s1 = "我是王二狗"
    for i in s1:
        # 将i这个数据，作为消息，存入到队列中
        q.put(i)
        time.sleep(random.random())



# 从队列中获取数据，并输出
def read_fn(q):
    print("我是获取数据的进程：%d" % os.getpid())
    while True:
        print("获取到的数据：", q.get())


if __name__ == "__main__":
    # step1.创建用于传递消息的队列
    q = Queue()

    # step2：创建子进程
    p1 = Process(target=write_fn, args=(q,))
    p2 = Process(target=read_fn, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    print("写入数据结束了。。")

    p2.terminate()
    print("读取数据结束了。。")
    print("主进程结束了。。")
