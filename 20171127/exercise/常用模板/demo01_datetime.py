"""
python的核心模块
1.日期：datetime,模块名
    <module 'datetime' from 'C:\\Python34\\lib\\datetime.py'>
    <class 'module'>
    类：datetime
        类属性：max，min
        类方法：now(),today(),获取当前的时间

        实例属性：
            年，月，日，时，分，秒，微秒
                year，month，day，hour，minute，second，microsecond
            星期：
                weekday，isoweekday


    时间戳：计算机中表示时间，其实是使用一个数字来表示(long类型的整数)
        1970年1月1日：0:0:0。基准值

        当前的日期距离基准值的时间。

        python的单位是秒，其他语言都是毫秒。

    格式化：

python中格式化日期：符号
%y, 两位数字，表示年份
%Y, 四位数字，表年份
%m, 表示月(01-12)
%d，表示日期(1-31)
%H, 时(0,23),
%M,分
%S,秒



1年365天：year
1天24小时：day
1小时：60分钟：hour
1分钟：60秒：minute
1秒：1000毫秒：
14:29:33.333

1毫秒：1000微秒
1微秒：1000纳秒
秒：s，毫秒：ms，微秒： (μs)，纳秒：ns
"""
from datetime import datetime


# print(datetime)  # <class 'datetime.datetime'>
# print(type(datetime))  # <class 'type'>

# 1.获取当前的时间
# time1 = datetime.now()
# print(time1)  # 2017-11-27 14:18:11.440000

# 2.获取指定的时间
# time2 = datetime(2017, 8, 23, 10, 4, 45)
# print(time2)

# 3.类属性：max，min。最大时间和最小时间
# print(datetime.max)  # 9999-12-31 23:59:59.999999
# print(datetime.min)  # 0001-01-01 00:00:00


# 4.实例属性，获取年，月date_msg = "年：%s，月：%s，日：%s，时：%s，分：%s，秒：%s，微秒：%s" % (time1.year, time1.month, time1.day, time1.hour, time1.minute, time1.second, time1.microsecond)
# print(date_msg)，日，时，分，秒。。
#



# 5.now()，today() 时区
# time3 = datetime.today()
# print(time3)


# 6.获取星期,weekday():返回是星期几(0-6), isoweekday():也是返回星期几(1-7)

# print(time1.weekday())
# print(time1.isoweekday())

# 7.时间戳：timestamp。
# 获取时间戳
# time_num = time1.timestamp()
# print(time_num)

# 将时间戳转为时间对象
# time3 = datetime.fromtimestamp(time_num)
# print(time3)

# 8.时间和字符串之间的 转换
# str1 = "2017-10-10"  # 字符串
# str2 = "2017年10月10日"
# 将给定的字符串，转为日期对象
# time4 = datetime.strptime(str1, "%Y-%m-%d")  # 格式化的模板，得字符串对应
# print(time4)


# 日期对象-->字符串
# time5 = datetime.now()
# print(time5)
# print(time5.__str__())   # 2017年11月27日,2017/11/27,2017-11-17
#
# str3 = time5.strftime(r"%Y-%m-%d")
# print(str3)
#
# str4 = time5.strftime(r"%Y年")
# print(str4)
"""
练习1： 2017-11-27
练习2: 14:30:44
"""

# time1 = datetime(2017, 11, 27)
# print(time1)
print(datetime.now())
print(datetime.now().timetz())


