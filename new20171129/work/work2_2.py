"""
提取url：以https开头，jpg结束
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">

"""
import re

str1 = """<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_smagll.jpg" 
src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_smagll.jpg" style="display: inline;">
"""
# url1 = re.search("https.+2016/", str1)
# url2 = re.search("11.+jpg", str1)
url = re.findall("https.+jpg", str1)
# print(url1.group() + url2.group())
print(url)
# print(url.group())


