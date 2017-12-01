"""
获取当前线程对象：current_thread()



"""
import threading
import time
import random

# 1.创建Thread类的子类
class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print("这是子线程：%s, i--->%d"% (self.name, i))
            print("1.获取线程的id号：", self.ident)
            print("2.线程的名称：", self.name)
            print("3.是否是守护线程：",self.isDaemon())
            # print("当前正在执行的线程对象：", threading.current_thread()) # -->t1
            time.sleep(random.random())



if __name__ == "__main__":
    t = threading.current_thread()  # 得到当前正在被执行的线程对象,主线程对象
    print("当前正在执行的线程对象名称：" , t.name)  # MainThread

    t1 = MyThread()  # 通过子类的方式创建的线程对象，不需要指明target对象，start启动后，自动run()
    t2 = MyThread()
    t3 = MyThread()
    t1.start()  # -->cpu-->run()
    # t2.start()
    # t3.start()

    # time.sleep(1)
    # t1.start()  # RuntimeError: threads can only be started once


"""
通过子类继承的方式，一个线程打印数字，一个线程打印字母
代码尝试：
    线程之间能否操作共享对象：全局变量
            全局变量
            子线程1：修改3次全局变量的数值
            子线程2：打印全局变量的值
            
            
"""