"""
创建一个列表，长度为10，数据是1-10的随机数。要求去重复
"""
import random

set1 = set()
while len(set1) < 10:
    set1.add(random.randint(1, 10))
print(set1)
print(list(set1))

