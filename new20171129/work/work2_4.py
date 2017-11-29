"""
有一句英文如下：

hello world ha ha

查找所有的单词
"""
import re

s1 = "hello world ha ha"
words = re.split("\s", s1)
print(words)
