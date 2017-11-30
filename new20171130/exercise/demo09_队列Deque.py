"""
队列：Queue，
    先进先出：FIFO

empty()
full()
qsize()
put([是否阻塞，timetout])
    默认是True，队列为满，处于阻塞
            设置timeout，
        设置为False
get([是否阻塞，timeout])
    默认是True，队列为空，处于阻塞状态，
            设置timeout，给定的时间内，阻塞，超时立刻异常
        设置为False，列队为空，立刻异常，不等待
"""
from multiprocessing import Queue

# 1.创建队列
q = Queue(3)  # 创建队列，3最大容量，

print("队列是否为空：", q.empty())
print("队列是否为满：", q.full())
print("队列的大小：", q.qsize())

q.put("消息1")  #
q.put("消息2")
print("队列的大小：", q.qsize())
print(q.full())
q.put("消息3")
print(q.qsize())
# q.put("消息4")  # 默认是阻塞式 方法。。
print("-" * 50)

print(q.get())  # 获取队头
print(q.qsize())
print(q.get())  # 消息二
print(q.get())

print(q.qsize())
# print(q.get())  # 默认是阻塞式，没有消息可以获取，就等待。。

print("*" * 50)


# print(q.get(True,2))  # queue.Empty

if q.full():
    q.get_nowait()  #

if not q.full():
    q.put_nowait() #