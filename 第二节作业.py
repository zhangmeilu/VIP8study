# 有三个办公室，8位老师，8位老师分配到3个办公室

import random

# 定义办公室和老师
office = [["办公室1"],["办公室2"],["办公室3"]]
teacher = []
# 循环添加老师
i = 0
while i < 8:
    teacher.append(f"老师{i + 1}")
    i += 1
# 随机添加老师进办公室
i = 0
while i < 8:
    # 随机抽老下标和办公室下标，randnit是闭区间
    o = random.randint(0,len(office)-1)
    t = random.randint(0,len(teacher)-1)
    # 添加到办公室
    office[o].append(teacher[t])
    # 添加完再列表里删掉那个老师，删除下标用pop或者del
    teacher.pop(t)
    del teacher[t]
    i += 1
print(office)


