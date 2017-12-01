"""
全局变量--->启动线程，执行方法(参数)
    A：数据类型：数据不可变？共享么？
    B：全局变量是list列表呢？共享么？

"""
from threading import Thread
import time

g_num = 100
g_list = [10, 20, 30]


def work1(num):
    for i in range(3):
        num += 1
        print("--子线程1--work1----num:%d" %num)


def work2(num):
    print("\t--子线程2---work2---num：%d" % num)


if __name__ == "__main__":
    print("主线程访问g_num:%d" % g_num)

    t1 = Thread(target=work1, args=(g_num,))
    t2 = Thread(target=work2, args=(g_num,))
    t1.start()  # ？
    time.sleep(1)

    t2.start()  # ?

