

from multiprocessing import Process
import os
import time


def test1():
    print("\t子进程：%d" % os.getpid())
    for i in range(10):
        print("\t子进程打印：%d" % i)
        time.sleep(1)


if __name__ == "__main__":
    pid = os.getpid()
    print("主进程pid：", pid)

    p1 = Process(target=test1)
    p1.start()

    time.sleep(2)
    p1.terminate()  # 结束子进程，无论子进程的任务是否做完。。
    print("主进程结束。。。")