"""
4个售票口，同时售出10张票。
    1-10

    锁对象：Lock

互斥锁：
    锁头对象：状态可以是打开，锁定。

    多线程访问共享数据的时候，造成该数据的不安全。--->临界资源问题：数据不安全问题

    使用同步：
        每次只允许一个线程来执行，不允许其他线程插入执行。

    实现：-->互斥锁：
    step1：导入模块threading 中Lock类
    step2：创建锁对象
        mutex = Lock()
    step2：上锁：acquire(词意：获取，获得)
        mutex.acquire()

    step3：开锁：release(词意：释放)
        mutex.release()


锁对象：
    被锁定：只有一个线程执行。
    打开锁：大家再抢占资源




"""
from threading import Thread, current_thread,Lock
import time
import random

tickets = 10  # 售票

mutex = Lock()  # 创建一个互斥锁：Lock的对象，代表锁头。默认状态是打开的。


def sale_tickets():
    global tickets

    while True:
        mutex.acquire()  # 表示上锁，以下的代码，每次只能被一个线程执行。
        if tickets > 0:
            # 睡眠
            time.sleep(random.random())
            print("%s，售出火车票：%d" % (current_thread().name, tickets))
            tickets -= 1
        else:
            break
        mutex.release()  # 表示开锁，

if __name__ == "__main__":
    t1 = Thread(target=sale_tickets, name="售票口1")
    t2 = Thread(target=sale_tickets, name="售票口2")
    t3 = Thread(target=sale_tickets, name="售票口3")
    t4 = Thread(target=sale_tickets, name="售票口4")
    t1.start()
    t2.start()
    t3.start()
    t4.start()




