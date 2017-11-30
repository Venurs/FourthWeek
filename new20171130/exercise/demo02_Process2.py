"""

"""
from multiprocessing import Process
import os
import time


def test1(num, str):
    print("\t子进程的pid：%d" % os.getpid())
    print("\t子进程接收到的参数：", num, str)
    for i in range(5):
        print("\t子进程。。%d" % i)
        time.sleep(1)


if __name__ == "__main__":
    # 1.打印主进程的pid
    print("main。。。pid：%d" % os.getpid())



    # 2.创建子进程
    """
    创建子进程对象：p1 = Process()
    第一个参数：target：目的，表示子进程要执行任务。(一个可执行的对象)
    第二个参数：name，进程的名字，如果不指定的，系统编号：Process-1,2,3...
    第三个参数：args，一个元组，表示要传递给target目标的参数。
    第四个参数：kw：关键字参数，字典
    第五个参数：group：绝大多数用不到
    """
    p1 = Process(target=test1, name="子进程", args=(1000, "王二狗"))
    # 3.启动子进程
    p1.start()
    # 4. 子进程的名字：
    print("p1子进程的进程名字：%s" % p1.name)

    p1.join()  # "合并，参加",等待子进程结束。。导致主进程阻塞(暂时不能执行),要等待子进程p1，结束后，解除阻塞
    print("主进程执行。。。")


    """
    主进程中启动了子进程，在子进程没有结束之前，主进程不会结束的。
    
    p.join(),子进程执行结束后，主进程才会继续执行。
    p.join(timeout),子进程结束了，那么解除阻塞，主进程继续执行。时间到也会解除阻塞，主进程还是会继续执行。。
    """
