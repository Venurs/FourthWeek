"""
正则的规则：
一.一般的符号
  1.字面量
  2..点代表1个任意字符，除\n外
  3.[],匹配[]中任意字符都可以
  4.[abc],匹配a或b或c。1位
  5.[a-z],匹配任意一位的小写字母
  6.[^abc],除abc外的任意一位字符
"""
import re

# # 1..代表匹配任意字符
# m1 = re.match("123.", "123*emeda")
# print(m1)
# m2 = re.match("123....", "123memeda")
# print(m2)
#
# # 2.[],匹配[]里的任意一个
# m3 = re.match("[abc]", "saaa")  # 或a或b或c开头即可。
# print(m3)
# m4 = re.match("a[abc]", "as")  # 第一个字母必须是a，第二个字符a,或b或c
# print(m4)
# m5 = re.match("[a-z]", "A23abc")  # 必须是小写字母开头
# print(m5)
# m6 = re.match("[a-zA-Z][a-z]c", "Abcabc")  # 字母
# print(m6)
# m7 = re.match("[0-9]", "110abc")  # 数字
# print(m7)
#
# m8 = re.match("[^abc]", "*&%ABC123abc")  # 非abc开头即可
# print(m8)
#
# m9 = re.match("[^a-z]", "memeda")
# print(m9)
# m10 = re.match("1[^2345]", "1a6")
# print(m10)
phone = re.match("1[34578]" + 9 * "\d", "18434367251")
print(phone)


