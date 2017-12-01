"""
4个售票口，同时售出10张票。
    1-10
"""
from threading import Thread, current_thread, Lock
import time

num = 10
lock = Lock()


def sale_ticket():
    while True:
        global num
        lock.acquire()
        if num <= 0:
            print("当前无票")
            lock.release()
            break
        # time.sleep(1)
        num -= 1
        print("%s售票成功，当前余票%d" % (current_thread().name, num))
        lock.release()


if __name__ == '__main__':
    for i in range(1, 4):
        th = Thread(target=sale_ticket, name="窗口" + str(i), args=())
        # time.sleep(2)
        th.start()
        th.join()

