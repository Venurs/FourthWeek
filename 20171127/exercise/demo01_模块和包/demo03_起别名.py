"""
起别名，但是如果使用了别名，就不能再使用原来的名字。

"""
import demo01_模块和包.a as CatMoudel
import demo01_模块和包.b as DogMoudel

CatMoudel.say_hello()  # 调用a模块


dog1 = DogMoudel.Dog()  # 穿件b模块的dog对象