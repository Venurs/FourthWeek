"""
进程池：pool
    理解为一个容器，该容器中有实现创建好的进程对象：
"""
from multiprocessing import Pool
import os

def foo(name):
    print("foo,", name)


if __name__ == "__main__":
    # 1.打印主进程的pid
    print("main....%d" % os.getpid())
    # 2.创建进程池：-->进程池创建成功，已经存在了进程对象。
    """
    Pool，表示进程池。事先已经存在了一些进程对象。直接分配任务即可
    第一个参数：numprocess，进程池中子进程对象的数量，
    第二个参数：子进程要执行的任务
    """
    pool1 = Pool(3, foo, ("王二狗",))  # 创建进程池，并且分配了任务，自动执行。。
    # step1：创建进程池，step2：apply(),apply_async()