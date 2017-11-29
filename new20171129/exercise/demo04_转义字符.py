"""
四、转义：\
    1.普通的字符-->特殊含义的字符
        n,r,t,b--->\n,\r,\t,\b
    2.特殊含义的字符-->普通字符
        ",',\-->\",\'

    "\"abc"-->"abc
    "\\abc"

转义字符和原始字符串
r""


\"-->"
\\-->\
\.-->.


\w,\d,\s,\b....-->正则中规定的字符


五、边界问题：
1.^,表示匹配的起始位置
2.$,表示结束的位置
"""
import re

m1 = re.match("\n\w", "\nabc")  # <_sre.SRE_Match object; span=(0, 2), match='\na'>
print(m1)
m2 = re.match("\n\w", "\\nabc")  # None
print(m2)
m3 = re.match("\\n\w", "\\nabc")  #None
print(m3)
m4 = re.match("\\\\n\w", "\\nabc")
print(m4)
m5 = re.match(r"\\n\w", "\\nabc")
print(m5)

m6 = re.match("\.\w+", ".abc")
print(m6)


# 边界问题
m7 = re.match("1[34578]\d{9}", "13278652345")
print(m7)
m8 = re.match("1[34578]\d{9}", "1327865234578484848955")
print(m8)
m9 = re.match("^1[34578]\d{9}$", "13278652345")  # ^可以不用，match()方法本身就是从头匹配
print(m9)


m10 = re.match("^[1-9]\d{17}$", "12345619881023432132")
print(m10)


# 单词边界 "today is good"   (空格/开头)单词(末尾空格/结束)
print(re.match("^\w+ve", "hover"))  # <_sre.SRE_Match object; span=(0, 4), match='hove'>
print(re.match("\w+ve", "hoverhoverhover"))

print(re.match(r"^\w+ve$", "hover"))  #  None
print(re.match(r"^\w+ve", "hover hover"))  # <_sre.SRE_Match object; span=(0, 4), match='hove'>
print(re.match(r"\w+ve\b", "hoverhover"))
print(re.match(r"\w+ve\b", "hove r"))  # today is good
print(re.match(r"^\w+\sve\b", "ho ve r"))  # None
# r"^balbal$"


