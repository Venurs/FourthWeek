"""
使用deque，完成学生姓名管理系统。
append(),appendleft()
pop(),popleft(),remove()
"""
from collections import deque


de = deque()


def append_de(name):
    while True:
        print("0:列表前添加；1：列表后添加")
        way = int(input("请输入您要添加的方式："))
        if way == 1:
            de.append(name)   # 从列表后面添加学生
            print("%s添加成功，添加方式append" % name)
            break
        elif way == 0:
            de.appendleft(name)  # 从列表前面添加学生
            print("%s添加成功，添加方式appendleft" % name)
            break
        else:
            print("输入有误，返回后重新输入。。。。")
            continue


def remove_de():
    while True:
        print("0:列表前删除；1：列表后删除")
        way = int(input("请输入您要删除的方式："))
        if not de:
            if way == 1:
                print("%s删除成功，删除方式pop" % de.pop()) # 从列表后面删除学生
                break
            elif way == 0:
                print("%s删除成功，删除方式popleft" % de.popleft())  # 从列表前面删除学生
                break
            else:
                print("输入有误，返回后重新输入。。。。")
                continue
        else:
            print("无法删除，列表为空")


def show():
    if not de:
        print("未添加任何学生")
    for stu in de:
        print(stu, end=" ")
    print()


while True:
    print("0:添加学生；1：删除学生;  2:显示所有学生")
    choose = int(input("请选择您要执行的操作："))

    if choose == 0:
        name = input("请输入要操作的学生的姓名：")
        append_de(name)
    elif choose == 1:
        remove_de()
    elif choose == 2:
        show()
    else:
        print("输入有误，返回后重新输入。。。。")
        continue



