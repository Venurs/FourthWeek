"""
线程是进程中一条执行路径：
    多线程：一个进程中多条线程

step1：导入模块，从threading模块中导入Thread类
    from threading import Thread

step2：创建线程对象
    t1 = Thread(target="",name="",args)

step3：启动线程：
    t1.start()
"""
from threading import Thread, current_thread
import time

#
# def say_sorry():
#     print("子线程的名称：%s" % current_thread().name)
#     time.sleep(0.1)
#     print("我错了，我可以起来了么，不想跪了。。对不起就完了呗")
#     time.sleep(2)
#
#
# if __name__ == "__main__":
#     print("主线程的名称：%s" % current_thread().name)  # MainThread
#     for i in range(5):
#         # 创建线程
#         t = Thread(target=say_sorry, name="线程"+str(i))
#         # 启动线程
#         t.start()


"""
current_thread()-->获取当前线程对象
    谁正在被cpu执行，谁就是当前线程对象
    
    进程名称：默认：Process-1,2,3.。。
    线程名称：默认：Thread-1,2,3.。。
    
练习1：
    创建2条线程：一个打印数字100个，一个打印字母100。观察打印结果。。  

"""


def put_dig():
    for i in range(1,100):
        print(i)
        time.sleep(2)


def put_letter():
    print(chr(100))
    time.sleep(2)


class PutDig(Thread):
    def run(self):
        for i in range(1, 100):
            print(i)
            time.sleep(2)


class PutLetter(Thread):
    def run(self):
        for i in range(97, 122):
            print(chr(i))
            time.sleep(2)


if __name__ == '__main__':
    # thread1 = Thread(target=put_dig, name="打印数字")
    # thread2 = Thread(target=put_letter, name="打印字母")
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    PutDig().start()
    PutLetter().start()


