"""
defaultdict，带默认值的字典。
    针对于dict，如果key不存在，获取key对应的value值，报错：KeyError。

defaultdict(函数)
    创建一个字典：如果key不存在，获取默认值:（函数的返回值作为默认值）
"""
from collections import defaultdict

#
# dict1 = {"name": "王二狗", "age": 30}
# print(dict1["name"])
# # print(dict1["aga"])  # KeyError: 'aga'
# # 字典名[key] = value。key不存在就添加名值对，如果key存在，就修改。
# print(dict1.get("name"))  # 存在就获取对应value值，不存在，返回None。
#
# def foo():
#     return "无结果"
#
#
# # dict2 = defaultdict(foo)  # {}
# dict2 = defaultdict(lambda : "无结果")
# print(dict2)  # {}
# print(dict2["name"])  # 获取key为name的值。如果没有就添加，value是默认值
# print(dict2)
# dict2["age"] = 30  # 添加名值对
# print(dict2)
# dict2["name"] = "李小花"
# print(dict2)
#
# print(dict2["name"])


print("-" * 50)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

for item in s:
    # print(item)
    color, count = item
    print(color, count)



# "yellow":[1, 3], blue:[2, 4],red:[1]

# dict3 = defaultdict(list)  # {}
# print(dict3["name"])  # []
# print(dict3)





