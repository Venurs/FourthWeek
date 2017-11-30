"""
进程之间传递消息：
    Queue，使用队列。只能够实现普通的进程之间传递消息。(由Process或其子类创建的进程对象)

进程池之间的进程传递消息：
    使用Queue，由Manager来创建的队列
"""
from multiprocessing import *

def write_fun(q):
    print("处理数据的进程：")
    for i in "王二狗":
        q.put(i)


def read_fun(q):
    print("获取数据的进程：")
    for i in range(q.qsize()):
        print("获取到的数据：", q.get())


if __name__ == "__main__":
    p = Pool()
    q = Manager().Queue()  # 由Manager类的对象，创建的队列，是进程池之间的进程传递消息使用的队列。
    # q = Queue() # -->普通进程之间传递消息的普通队列
    # apply(),apply_async()
    p.apply(write_fun, (q,))
    p.apply(read_fun, (q,))

    print("主进程也结束了。。")