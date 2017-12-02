"""
打印当前的日期,并计算出距离1970年1月1日0时0分0秒有几天几时几分几秒
"""
from _datetime import datetime

now = datetime.now()
print(now)

second = datetime.timestamp(now)
print(second)
day = second // (60 * 60 * 24)
hour = (second % (60 * 60 * 24)) // (60 * 60)
minute = (second % (60 * 60 * 24) % (60 * 60)) // 60
second1 = ((second % (60 * 60 * 60 * 24)) % (60 * 60)) % (60 * 60)
print("%d天%d时%d分%d秒" % (day, hour, minute, second1))


