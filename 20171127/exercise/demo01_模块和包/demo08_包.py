"""
包：package
    1.概念
        包就是包含多个模块的一个特殊的目录
        目录下有__init__.py的文件
        包名的命名方式，满足标识符命名规范，字母小写，下划线链接

    2.导入包
        A：导入包下某个模块
            import 包名.模块名

        B：导入该包下的所有文件
            from 包名 import *
            设置包下的__init__.py,导入包的时候初始化文件。
                需要提供可以使用的模块列表
                    from . import 模块
                    __all__ = ["模块名", "模块名"]
"""
import test包.d
from test包 import *

test包.d.test1()

e.test2()
