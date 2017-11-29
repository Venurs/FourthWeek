"""
Counter：计数器(简单的计数器)
    统计集合中元素出现的次数
        key，value
        元素，次数
        元素，次数
        。。。
    -->counter继承dict。key，value

一、创建计数器对象：
    Counter(iterable) -- >计数器对象：{元素：次数}
    Counter(dict)
    Counter(关键字参数)

二、方法
    elements()-->可迭代对象
        sorted(elements())-->list
    most_common(n)
"""
from collections import Counter

# print(Counter)
# print(type(Counter))
# print(issubclass(Counter, dict))  # True
#
# # 1.创建一个counter(string)-->计数器对象：统计字符串中每个字符出现的次数
# c1 = Counter("a4bcaababc39884443abc")  # Counter({'a': 5, '4': 4, 'b': 4, 'c': 3, '3': 2, '8': 2, '9': 1})
# print(c1)
#
# c2 = Counter([10, 20, 10, 20, 10, 30, 10])  # Counter({10: 4, 20: 2, 30: 1})
# print(c2)
#
# # 2.直接通过字典
# c3 = Counter({"a": 3, "b": 6, "c": 2})  # Counter({'b': 6, 'a': 3, 'c': 2})
# print(c3)
#
# # 3.通过关键字参数
# c4 = Counter(a=3, b=6, c=2)  # Counter({'b': 6, 'a': 3, 'c': 2})
# print(c4)
#
# # 4.elements()-->iterable,将计数器对象-->可迭代对象，for in遍历
# print(c1)
# it1 = c1.elements()  # a:计时器对象-->可迭代对象(每个元素)
# for i in it1:
#     print(i)  # 遍历元素，根据元素的次数遍历
#
# list1 = sorted(c1.elements())  # b：可迭代对象，进行排序-->list
# print(list1)
#
# # 5. most_common(n)
# print(c1)
# print(c1.most_common(3))
#
#
# list2 = sorted(c3.elements())
# print(list2)


"""
练习1：给定字符串"qwe5hhddjUEEHEHdjekjrjr838747472827373bdbhhdbehBDEHBDu3uddjf",每个字符出现的次数
练习2：给定一个列表：["Rose", "Jack", "王二狗", "王二狗", "Rose", "Jerry", "Rose"]
    每个人名出现的次数
    获取次数最多一个名字
"""
str1 = "qwe5hhddjUEEHEHdjekjrjr838747472827373bdbhhdbehBDEHBDu3uddjf"
cou = Counter(str1)
print(cou)
it = cou.elements()
for i in it:
    print(i, end=" ")
print(cou.most_common(3))


list1 = ["Rose", "Jack", "王二狗", "王二狗", "Rose", "Jerry", "Rose"]
cou2 = Counter(list1)
print(cou2)
it1 = cou2.elements()
for i in it1:
    print(i, end=" ")



