"""
有一批网址：
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
需要 正则后为：
http://www.interoem.com/
http://3995503.com/
http://lib.wzmc.edu.cn/
http://www.zy-ls.com/
http://www.fincm.com/
"""
import re

s1 = "http://www.interoem.com/messageinfo.asp?id=35"
s2 = "http://3995503.com/class/class09/news_show.asp?id=14"
s3 = "http://lib.wzmc.edu.cn/news/onews.asp?id=769"
s4 = "http://www.zy-ls.com/alfx.asp?newsid=377&id=6"
s5 = "http://www.fincm.com/newslist.asp?id=415"

addrs = [s1, s2, s3, s4, s5]
for addr in addrs:
    addr = re.match(".+(com|cn)", addr)
    print(addr.group())


