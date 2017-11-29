"""
创建一个列表，长度为10。数据是1-100内的随机偶数
"""
import random

list1 = []
for i in range(1, 11):
    list1.append(random.randrange(2, 100, 2))
print(list1)


