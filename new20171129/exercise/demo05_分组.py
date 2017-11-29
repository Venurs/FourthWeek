"""
六、分组：
    1.|,或者的意思
        a|b,a或者b
    2.(),代表了分组
        (abc)-->一组
        正则表达式中使用了分组，组默认是有编号的：1,2,3.。。
    3.\num,引用分组的内容
        num是分组的编号
    4.(?P<name>),给分组起别名
    5.(?P=name),引用分组
        P字母大写

group()-->获取匹配上的内容

"""
import re
print(re.match("[0-9]|x", "x"))
print(re.match("[ab]", "a"))
print(re.match("abc|ddd", "ddd"))

# 身份证：第一位：非0,16位。最后一位：(数字|X)
print(re.match("[1-9]\d{17}|[1-9]\d{16}X", "23141219880712321X"))
print(re.match(r"^[1-9]\d{16}(\d|X)$", "23141219880712321X"))


# 练习2：邮箱：163.com，qq.com?
s1 = "wangergou@163.com"
s2 = "sanpang@qq.com"  # 828384848@qq.com
s3 = "lixiaohua@sina.com"

print(re.match(r"\w+@(163|qq)\.com", s3))

#  练习3：邮箱：163.com,sina.cn,yahoo,cn,qq.com
print(re.match(r"\w+@(163|sina|yahoo|qq)\.(com|cn)", "sanpang@163.com"))

s4 = "<html><h1>helloworld</h1></html>李小花李小花"
m4  = re.match(r"<(.+)><.+>(.+)</.+></.+>", s4)  #
print(m4)
print(m4.group(1))
print(m4.group(2))

s5 = "<html><h1>memeda</abc></ddd>"
m5 = re.match(r"<(.+)><(.+)>(.+)</\2></\1>", s4)
print(m5)
print(m5.group())  # group()，默认参数是0，代表匹配上的整体：<html><h1>helloworld</h1></html>
print(m5.group(1))  # html
print(m5.group(2))  # h1
print(m5.group(3))  # helloworld


s6 = "<html><body><h1>hello</h1></body></html>"
print(s6)
m6 = re.match(r"<(.+)><(.+)><(.+)>(.+)</\3></\2></\1>", s6)
print(m6)
print(m6.group(4))
m7 = re.match(r"<(?P<t1>.+)><(?P<t2>.+)><(?P<t3>.+)>(?P<t4>.+)</(?P=t3)></(?P=t2)></(?P=t1)>", s6)
print(m7)
print(m7.group("t3"))
print(m7.group("t4"))

res = m7.groups()
print(type(res))
print(res)

