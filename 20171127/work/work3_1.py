"""
拼接一个字符串，长度为4。其实就是随机生成验证码

内容是26个小写字母和26个大写字母。以及0-9数字。
0-9-->数字的编码是：[48,57]
a-z-->小写的编码是：[97,122]
A-Z-->大写的编码是：[65,90]
"""
import random
str1 = ""
for i in range(48, 58):
    str1 = str1 + chr(i)
for i in range(97, 123):
    str1 = str1 + chr(i)
for i in range(65, 91):
    str1 = str1 + chr(i)
print(str1)
print(random.sample(str1, 4))
