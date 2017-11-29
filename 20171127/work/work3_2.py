"""
创建一个列表，长度为10，数据是1-10的随机数。要求去重复
"""
import random


list1 = []
while len(list1) < 10:
    num = random.randint(1, 10)
    if num in list1:
        continue
    list1.append(num)
print(list1)

