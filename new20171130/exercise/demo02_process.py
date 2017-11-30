"""
多任务，也叫多进程（同时执行多个程序）
启动某一个程序，自己创建一主进程
    主进程中，可以自己创建子进程。
    step1：导入模块
        from multiprocessing import Process

    step2：创建Process类的对象，代表子进程

    step3：启动子进程，表示可以让cpu调度执行


p1,表示子进程，在主进程中创建并启动
    主进程：父进程
    子进程：子进程
"""
from multiprocessing import Process
import time
import os

# def test():
#     while True:
#         print("\t\t我在子进程中执行了。。子进程的pid：%d， 父进程的pid：%d" % (os.getpid(), os.getppid()))
#         time.sleep(1)
#
# if __name__ == "__main__":
#     print("主进程的pid：%d" % os.getpid())
#
#     # 1.创建子进程对象：使用关键字参数target指明该子进程中要执行的内容
#     p1 = Process(target=test)  # 指明该进程被cpu调度执行的时候，执行哪些代码-->函数
#     # 2.启动子进程
#     p1.start()
#
#     while True:
#         print("---main----")
#         time.sleep(1)

"""
1.先创建主进程：
    A:创建子进程
    B：启动子进程
    
主进程不能早死于子进程：
"""


"""
子进程中打印数字：1-1000
主进程中打印字母：A

获取进程的pid
"""


def put_num():
    for i in range(1, 1000):
        print(i, end=" ")


if __name__ == '__main__':
    print("A")
    print(os.getpid())
    p = Process(target=put_num)
    p.start()
    if p.is_alive():
        print("B")
    print(current_process())
    # p.join()


