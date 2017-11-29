"""
创建一个列表，长度为10，数据是1-10的随机数。要求去重复
"""
import random


def product(n):
    list1 = []
    while len(list1) < 10:
        num = random.randint(1, n)
        if num in list1:
            continue
        list1.append(num)
    return list1
print(list1)

