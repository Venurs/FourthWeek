"""
三、数量词
    1.*，出现的次数是0次或多次
    2.+,出现的次数是1次或多次
    3.?,出现的次数是0次或1次
    4.{M}，出现的次数刚好是m次
    5.{M,},至少M次
    6.{M,N},至少m次，至多n次
"""
import re
# m1 = re.match("\d*", "123")
# print(m1)
# print(m1.group())
#
# m2 = re.match("\d*", "abc123")
# print(m2)
#
# m3 = re.match("\d*", "")
# print(m3)
#
# m4 = re.match("a[b-f]*\d\d[xy]*", "abbbb123x")  # 至少0位，意味着可以没有
# print(m4)
# m5 = re.match("a[b-f]*\d\d[xy]*", "a12xxyxx3x")
# print(m5)
#
# m6 = re.match("\d+abc", "abcmemeda")  # +至少一位
# print(m6)
#
# m7 = re.match("\d+.*\w+", "1234\ncd")
# print(m7)
#
# m8 = re.match("\d?[a-z]+", "123abc")
# print(m8)
# m9 = re.match("\d?\w+", "123abc")
# print(m9)
#
# m10 = re.match("\d{4}[a-z]+", "1234abcd")  # \d刚好4次
# print(m10)
#
# m11 = re.match("\d{4,}[a-z]+", "12345abcd")  # \d至少4次
# print(m11)
#
# # +-->1次或多次，至少1次{1,}
#
# m12 = re.match("\d{4,6}[a-z]+", "1234567abcd")
# print(m12)

# ?-->0次或1次，{0,1}

"""
练习1：日期：2017-11-29
    年份是4位数字，月份是1-2位数字，日期1-2位数字
练习2：邮箱：163.com，qq.com?

练习3：身份证号：18位。0不能开头
"""
date = re.match("\d{4}-\d{2}-\d{2}", "2017-01-29")
print(date)
mail = re.match(".+[].com", "manassehlost163q.com")
print(mail)
id_num = re.match("\d{18}", "610528199511104812")

print(id_num)

