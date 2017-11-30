s1 = """
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
"""
# 1.提取url：统一资源定位符：http://www.baidu.com
import re

r1 = re.search(r"https://.+?\.jpg", s1)
print(r1.group())

# 2.
s2 = """
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
def my_repl(m1):
    return m1.group(1)


s3 = re.sub(r"(http://.+?/)(.*)", lambda m1: m1.group(1), s2)
print(s3)


s4 = "hello  world      ha ha"
#  切割
list1 = re.split(" +", s4)
print(list1)

# 查找
list2 = re.findall(r"\b[a-zA-Z]+\b", s4)
print(list2)