"""
导入模块的搜索路径

__name__，获取模块名
    主模块：main,导入模块：导入模块名
__file__，导入模块的位置


自定义模块：
    1.模块名是标识符，要满足标识符的命名规范
    2.模块中：函数，和类
    3.语法：import 模块名
        from 模块名 import
    4.模块名：__name__
    5.扩展：
        A：__file__,导入的模块的位置
        B：搜索路径：sys.path。
        C：sys.path.appen()
"""
import random
import demo01_模块和包.a
import sys

# ran_num = random.randint(1, 5)
# print(ran_num)

print(random.__file__)  # C:\Python34\lib\random.py
print(demo01_模块和包.a.__file__)  # C:\Ruby\workspace\PycharmProjects1701\day16_模块和包\demo01_模块和包\a.py


# print(sys.path)  # 列表，导入模块的搜索顺序。
"""
['C:\\Ruby\\workspace\\PycharmProjects1701\\day16_模块和包\\demo01_模块和包', 
'C:\\Python34\\lib\\site-packages\\pip-9.0.1-py3.4.egg', 
'C:\\Ruby\\workspace\\PycharmProjects1701\\day16_模块和包', 
'C:\\Windows\\system32\\python34.zip', 
'C:\\Python34\\DLLs',
 'C:\\Python34\\lib',
  'C:\\Python34',
   'C:\\Python34\\lib\\site-packages']
"""