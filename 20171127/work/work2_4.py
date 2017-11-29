"""
打印当前的日期，按照指定的格式：
格式1:2017年11月27日
格式2:2017-11-27
格式3:2017-11-27 16:33:44
格式4:16:33:44

让当前的程序睡眠5秒钟，再运行后面的代码
"""
from datetime import datetime
import time

time1 = datetime(2017, 11, 27, 16, 33, 44)
print("%s年%s月%s日" % (time1.year, time1.month, time1.day))
print("%s-%s-%s" % (time1.year, time1.month, time1.day))
time.sleep(5)
print("%s-%s-%s  %s:%s:%s" % (time1.year, time1.month, time1.day, time1.hour, time1.minute, time1.second))
print(time1.timetz())

