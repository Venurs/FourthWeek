"""
正则表达式(regular expression)
    retular:词意:正则，正规，规则，规律
    expression：表达式

    用途：使用正则表达式验证文本(字符串)是否满足指定的规则

step1：导入re模块

step2：调用方法
    re.match(pattern,string)
    re.search(pattern，string)

step3：获取结果
    group()
"""
import re

# 1.使用match(规则，文本字符串),表示匹配使用规则，验证字符串是否满足的。
# 执行：从左侧开始来匹配，如果匹配成功就返回match对象，如果不匹配，就返回None
m1 = re.match("foo", "foo_test")
print(m1)  # <_sre.SRE_Match object; span=(0, 3), match='foo'>
print(type(m1))  # <class '_sre.SRE_Match'>
print(m1.group())  # 获取匹配 上的内容

m2 = re.match("foo", "test_foo")
print(m2)  # None,匹配失败

# 2.search(),搜索,字符串中任意位置匹配上都可以。
m3 = re.search("foo", "hellofoo_test")
print(m3)
print(m3.group())
