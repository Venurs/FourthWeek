"""
namedtuple()
    是一个函数。创建一个自定义的tuple对象。
        可以给tuple元素起名字，也可以定义元素的个数。

        理解为：相当于类的tuple

tuple：元组
    有序，不能修改。(10,20)


namedtuple,具有了tuple的不可变性，然后又可以操作属性，方便，清晰。

操作：
    获取数据：
        tuple：仅通过下标
        namedtuple：通过下标，还可以通过属性

    其他方法：了解
        _replace()-->替换某些属性值，产生新的对象
        _make()-->产生新的对象
        _asdict()-->获取OrderedDict，获取有序字典

    属性：
        _fields:
        _source:class Point(tuple)

"""
from collections import namedtuple

#
# print(namedtuple)  # <function namedtuple at 0x00000000023CBE18>
# print(type(namedtuple))  # <class 'function'>
#
# Point = namedtuple("Point", ["x", "y"])  # 自定义的元组类型
# print(Point)
# print(type(Point))
# print(issubclass(Point, tuple))  # True
#
# # 1.创建元组来存储数据
# tuple1 = (10, 20)
# p1 = Point(10, 20)
# print(tuple1)
# print(p1)
# p2 = Point(x=10, y=20)
# print(p2)
#
# # 2.获取数据
# print(tuple1[0])  # tuple只能通过下标获取存储的数据
# print(p1[0])  # 通过下标获取
# print(p1.x)  # 通过属性名获取数值
#
#
# # 3.修改：无论是tuple，还是Point都不允许修改。
# # Point，理解是tuple的子类。
# # tuple1[0] = 100
# # p1.x = 100
# # print(p1)
#
# # 4.实例方法_replace(),修改某个属性的值，但是返回一个新的对象。
# p2 = p1._replace(y="a")
# print(p1)
# print(p2)
#
# # 5.扩展：_make()，也可以用于创建Point对象。参数是Iterable：序列
# p3 = Point._make([100, 200])
# print("-------------")
# print(p3)
#
# # 6._asdict() ,OrderedDict
# """
# 有序列表，无序列表
# """
# d3 = p3._asdict()
# print(d3)
#
# # 7.属性
# print(Point._fields)  # ('x', 'y')
# # 8.源代码
# print(Point._source)

Point = namedtuple("Point", ["x", "y", "z"])
p1 = Point(10, 20, 30)
for i in p1:
    print(i)
p2 = p1._replace(x=20)
print(p2.x)







