"""
进程池：的操作步骤：
step1：创建进程池对象
    p1 = Pool(num)-->num是进程池中的进程的数量

step2：分配任务
    apply_async()，异步
    apply(),了解，同步：one by one

小花等二狗一起吃饭，二狗去厕所了，小花要吃饭

同步：one by one
    step1：小花等二狗一起吃饭
    step2：二狗去厕所了
    step3：小花要吃饭
轮询：
    step1：小花等二狗一起吃饭
    step2：二狗去厕所了
    反复的来询问二狗是否回来。。。

异步：效率高
    step1：小花等二狗一起吃饭
    step2：二狗去厕所了，小花要吃饭
"""
from multiprocessing import Pool
import os
import time

def foo(num):
    for i in range(5):
        print("--pid:%d, --num:%d, --i:%d, "% (os.getpid(), num, i))
        time.sleep(2)
    return num ** 2

if __name__ == "__main__":
    # 1.创建一个进程池,该进程池中有3个进程对象，等待干活
    pool1 = Pool(3)

    # 2.给进程池分配任务
    for x in range(5):  # x:01234
        a = pool1.apply_async(foo, (x,))  # 主进程使用apply_async()给进程池中的进程对象分配任务。存在返回值：ApplyResult
        # print(a)  # ApplyResult
        # print(type(a))
        # print(a.get(), a.successful())

    # 关闭进程池，不给进程池再分配任务了。
    pool1.close()
    pool1.join()  # 如果没有join().，那么主进程结束后，子进程也结束了，可能任务没有执行完毕
    print("子进程结束。。。")
    print("主进程也结束。。")