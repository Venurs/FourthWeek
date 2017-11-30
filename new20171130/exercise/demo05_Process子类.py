"""
多进程：也叫多任务
    创建进程的方式：
    1.其他的操作系统(Linux，mac等。。windows除外),os.fork()
    2.使用multiprocessing包下Process类
        创建Process类的对象，就是创建一个进程的对象，start()
        p1 = Process(target)-->进程的时候，要执行的目标代码
    3.创建子类，继承Process
        run()
    
"""
from multiprocessing import Process
import os
import time

# 1.定义子类，用于进程类
class MyProcess(Process):

    """
    Process父类，有没有__ini__()方法。MyProcess子类重写init方法。应该调用Process类init()
    """

    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    # 重写run()
    def run(self):
        t_start = time.time()
        for i in range(10):
            print("\t---MyPrcess---,pid:%d---i:%d" % (os.getpid(), i ))
            time.sleep(self.interval)
        t_end = time.time()
        print("\t子进程执行共耗时：%.4f" % (t_end - t_start))

if __name__ == "__main__":
    print("主进程：pid：%d" % os.getpid())
    # 1.创建子进程对象
    p1 = MyProcess(0.5)
    p1.start()  # 创建一个进程对象的时候：可以使用target来指明子进程要执行的内容。对于没有指明target内容的子进程，那么在start启动后，会自动的执行run()
    # print(p1.is_alive())
    p1.join()
    # p1.run()  # 对象执行方法，
    print("子进程结束，主进程也结束。。")