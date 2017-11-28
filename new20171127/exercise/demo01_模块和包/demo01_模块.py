"""
一、模块(moudle)
        所谓模块，就是指封装好一定功能的py文件。要想使用这些功能，直接导入模块即可。

        在python开发中，每一个py文件，都可以看做是一个模块。模块名其实就是文件名(不要后缀)

        模块中：全局变量的定义，功能函数的实现，类的定义。。

        分类：
            第一种：自己写的
            第二种：python自带的。安装好python安装包，自带一些模块，比如random，math，sys，datetime。。。。
            第三种：第三方的模块。。需要先安装：pip模块管理工具。

二、使用模块
    step1：先创建一个fibo.py的文件，作为模块，定义了一些功能函数

    step2：创建demo01.py文件，作为主程序，(主函数)

    step3：在demo01.py文件，导入fibo模块
        语法：import 模块名，模块名2
import 模块1
import 模块2


"""
import fibo

fibo.fib(8)
