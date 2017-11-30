from multiprocessing import Pool
import os
import time

def foo():
    for i in range(5):
        print("\t...pid%d, i:%d" % (os.getpid(), i))
        time.sleep(1)


if __name__ == "__main__":
    # 1.创建进程池
    p2 = Pool(3)

    # 2.分配任务：apply()
    for x in range(5):

        p2.apply(foo)  # 同步，子进程是一个一个执行的。阻塞的方式


    """
    主进程中创建进程池，进程池中有进程对象：子进程
    apply(),同步：阻塞，主进程中为子进程分配任务，启动子进程的执行。
        子进程一个一个顺序来执行，最后是主进程
        
    apply_async(),异步，非阻塞。
    """

    print("主进程结束。。")
