"""
使用namedtuple创建一个平面的圆。
3个属性值：x，y表示圆心位置，r表示半径
"""

from collections import namedtuple


Circle = namedtuple("Circle", ["x", "y", "r"])
circle = Circle(2, 3, 5)


