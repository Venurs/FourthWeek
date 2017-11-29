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

附加：
	Rose，Jack票数相同。？

ballot："选票"
vote：选举
"""
from collections import Counter
# step1.初始化候选人的信息
list1 = ["Rose", "Jack", "王二狗", "李小花", "三胖"]

# 投票
def vote():
    print(list1)
    list2 = []  # 投票的信息
    while True:
        ballot = input("请输入候选人姓名，over表示结束：")
        if ballot == "over":
            print("投票环节结束。。")
            break
        if ballot in list1:
            list2.append(ballot)
        else:
            print("%s，没有该候选人，此票无效" % ballot)
    return list2


# 获取结果
def get_result():
    while True:
        list2 = vote()  # []
        if not list2:
            print("此次投票异常。。")
            return
        print("投票的信息：", list2)
        # 统计票数
        c1 = Counter(list2)
        print(c1)
        # 获取最高票

        most_ballot = c1.most_common(1)[0][1]  # [('三胖': 3) , ('Rose': 2)]

        sum = 0  # 获取最高票数的同学人数
        for i in c1.values():
            if i == most_ballot:
                sum += 1

        if sum == 1:
            name = c1.most_common(1)[0][0]
            print("%s 同学，以最高票数%d，当选班长，鼓掌，撒花。。。" % (name, most_ballot))
            break
        else:
            print("%d 位同学均获取最高票数%d，请大家重新投票" % (sum, most_ballot))
            # 修改候选人的信息的列表
            list1.clear()
            list3 = c1.most_common(sum)
            for i in list3:
                list1.append(i[0])


get_result()