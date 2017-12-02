"""
随机生成10个1到100的随机数，并将它们从大到小排列
"""


import random
lists = []
for i in range(1, 11):
    lists.append(random.randint(1, 100))
print(sorted(lists, reverse=True))

