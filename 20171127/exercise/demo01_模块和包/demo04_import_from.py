"""
导入：
    import 模块名
        导入该模块下的所有内容。

        模块名.函数名()

导入部分：
    from 模块 import 变量名，函数名，类名

from 模块 import *
    *，通配符，导入该模块的所有内容
    函数名()
"""
from demo01_模块和包 import Cat, title
from demo01_模块和包 import say_hello as hello1
from demo01_模块和包 import say_hello as hello2

from multiprocessing import Process

# 导入的内容，存在重名的情况，后导入的会覆盖之前导入的。

cat1 = Cat()
print(cat1)
# say_hello()  # 调用a模块的sayhello函数

hello1()

hello2()

"""
练习1：熟悉import 的语法
练习2：熟悉from xxx import xx的语法
"""



