"""
random模块：随机
1.random(),获取一个[0,1）之间的小数，
2.randint(a, b),获取一个[a,b]的整数, a小于等于b
    a <= num <= b
3.uniform(a,b),获取一个[a,b]的小数。
    a <= num <= b
    b <= num <= a
4.randrange(start,stop,step),获取指定范围的随机数。范围是 根据起始值，结束值，以及步长，计算来的。

5.random.choice(sequence)序列中获取随机内容
    sequence：字符串，列表，元组

6.random.shuffle(list),列表打乱

7.random.sample(list,个数),取样
"""
import random

# .1获取随机小数
# num1 = random.random()  # 获取一个随机小数：[0,1)  0 <= num1 < 1
# print(num1)
#
# # 2.随机整数
# num2 = random.randint(1, 10) # 获取一个随机整数：1 <= num2 <= 10
# print(num2)
# num3 = random.randint(10, 10)
# print(num3)
#
# # 3.获取指定范围的随机小数
# num4 = random.uniform(1, 10)  # 获取[1,10]之间的小数
# print(num4)
# num5 = random.uniform(10, 1)
# print(num5)
#
# # 4.在指定的范围获取,randrange(start,stop,step)
# num6 = random.randrange(1, 10, 2)  # [1, 3, 5, 7, 9]
# print(num6)
#
# # 1-50的偶数：2,4,6,8...50
# num7 = random.randrange(2, 50, 2)
# print(num7)
#
# # 5.从指定的序列中获取：字符串，列表，元组
# s1 = "王二狗喜欢李小花，他们俩都喜欢学python"
# print(random.choice(s1))
# list1 = ["Rose", "王二狗", "Jack", "Jerry", "Tom"]
# print(random.choice(list1))
#
# # 6.将列表随机打乱,shuffle,词意："洗牌"
# random.shuffle(list1)
# print(list1)
#
# # 7.random.samle(列表，个数),随机取样
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list3 = random.sample(list2, 30)
# print(list2)
# print(list3)


# list2 = {
#     1: "史大光",
#     2: "曲义龙",
#     3: "liuyanan"
# }
# print(list2)
str1 = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
list1 = list(str1)
print(random.sample(list1, 4))

