"""
匹配出163的邮箱地址，且@符号前有4-20位。例如hello@163.com
"""
import re


mail1 = "1411716329@163.com"
mail_163 = re.match(r"\w{4,20}@163\.com", mail1)
print(mail_163.group())



