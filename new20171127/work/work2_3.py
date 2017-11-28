"""
打印当前的日期
"""
from datetime import datetime

time1 = datetime.today()
msg = "%s-%s-%s" % (time1.year, time1.month, time1.day)
print(time1)
print(msg)
