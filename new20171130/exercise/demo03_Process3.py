"""
p1.is_alive()：进程是否存活
p1.join():等待子进程结束。。
p1.terminate(),结束子进程
"""
from multiprocessing import Process
import time
import os


# 两个子进程将会调用的两个方法
def worker_1(interval):
    print("worker_1,父进程(%s),当前进程(%s)"%(os.getppid(), os.getpid()))
    t_start = time.time()  # 获取当前的时间
    time.sleep(interval)  # 程序将会被挂起interval秒
    t_end = time.time()  # 获取当前的时间
    print("worker_1,执行时间为'%0.2f'秒" % (t_end - t_start))


def worker_2(interval):
    print("worker_2,父进程(%s),当前进程(%s)" % (os.getppid(), os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_2,执行时间为'%0.2f'秒" % (t_end - t_start))


if __name__ == '__main__':  # 判断是否为主程序
    # 输出当前程序的ID
    print("进程ID：%s" % os.getpid())

    """
    创建两个进程对象，target指向这个进程对象要执行的对象名称，
    args后面的元组中，是要传递给worker_1方法的参数，
    因为worker_1方法就一个interval参数，这里传递一个整数2给它，
    如果不指定name参数，默认的进程对象名称为Process-N，N为一个递增的整数
    """
    p1 = Process(target=worker_1, args=(2,))
    p2 = Process(target=worker_2, name="王二狗", args=(1,))

    # 使用"进程对象名称.start()"来创建并执行一个子进程，
    # 这两个进程对象在start后，就会分别去执行worker_1和worker_2方法中的内容
    p1.start()
    p2.start()

    # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
    # p2.join()
    print("p2.is_alive=%s " % p2.is_alive())

    # 输出p1和p2进程的别名和pid
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)


    """
    join括号中不携带参数，表示父进程在这个位置要等待p1进程执行完成后，再继续执行下面的语句，一般用于进程间的数据同步
    如果不写这一句，下面的is_alive判断将会是True，
    改成p1.join(1)，
    因为p2需要2秒以上才可能执行完成，父进程等待1秒很可能不能让p1完全执行完成，所以下面的print会输出True，即p1仍然在执行
    """
    p1.join()
    print("p1.is_alive=%s" % p1.is_alive())
