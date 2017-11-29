"""
step1：初始化候选人的信息：
[Rose，Jack，王二狗，李小花，三胖]

step2：投票：
[]
Rose
Jack
Rose
Jack
Rose
Rose
Rose1-->无效
如花-->无效
弃权-->无效
[Rose,Jack,Rose,Jack,Rose,Rose]

step3：公布结果
Rose当先班长，鼓掌，撒花。。
"""
from collections import Counter
from random import choice

candidate = ["Rose", "Jack", "王二狗", "李小花", "三胖"]
count = 0
while True:
    count += 1
    vote = []
    for i in range(1, 31):
        vote.append(choice(candidate))
    c = Counter(vote)
    candidate.clear()
    name1, num1 = c.most_common(1)[0]
    print("第%d次投票结果:" % count)
    for i in c.most_common():
        name, num = i
        if num == num1:
            candidate.append(name)
        print(name, num, end="   ")
    print()
    if len(candidate) == 1:
        print("第%d次选举，最终班长是%s" % (count, candidate[0]))
        break



