"""
deque：双端队列
    double-ended queue

    可以操作两端
    双向链表：数据靠链表
        特点：删除和添加元素效率较高，但是遍历的效率相对低。

对比list：列表
    线性结构：数据连续存储
        特点：遍历的效率较高，删除和添加元素，效率相对较低。

一、创建
    deque(iterable , maxlen)

二、操作
    常用操作：
        append()
            appendleft()
        remove()
        insert()
        pop()
            popleft()

    其他操作：
        reverse()
        clear()
        extend()
        count()

结论：
    list和deque，用途：都是容器，特点都是有序，可以重复，可以修改。
        底层的实现不同：
            list：线性结构：遍历效率高
            deque：双端队列，插入和删除元素效率高
"""
from collections import deque

print(deque)  # <class 'collections.deque'>
print(type(deque))  # <class 'type'>


# 1.创建队列:deque(iterable, maxlen)
deque1 = deque([10, 20, 30, 40])
print(deque1)

deque2 = deque([10, 20, 30, 40, 50], 3)
print(deque2)

# 2.操作队列
# A:添加元素
deque1.append("a")  # 向队列末尾添加元素
print(deque1)
deque1.appendleft("b")  # 向队头添加元素
print(deque1)

# B:删除
e1 = deque1.pop()  # 删除队尾元素
print(e1)
print(deque1)
e2 = deque1.popleft()  # 删除队头元素
print(e2)
print(deque1)

#  C：remove
deque1.remove(20)  # ValueError: deque.remove(x): x not in deque,删除的指定元素不存在，那么异常
print(deque1)

# D：清除：clear()
deque1.clear()
print(deque1)

list1 = [10, 20, 30]
list1.append(40)
print(list1)
list1.pop()
print(list1)

# list1.remove(40)  # ValueError: list.remove(x): x not in list
print(list1)


print("-" * 50)
deque3 = deque([1, 2, 3, 3, 2, 1, 5])
print(deque3)
count1 = deque3.count(2)  # 统计元素出现的次数
print(count1)

# reverse()
deque3.reverse()
print(deque3)

# extend()
deque4 = deque(["a", "b"])
deque3.extend(deque4)
print(deque3)


# 属性：
print(deque2.maxlen)



deque1.insert(0, 100)

"""
练习1：创建队列：deque
练习2：常用的操作：增加，删除，修改元素，遍历。。
"""
