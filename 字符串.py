from random import random

name = '0123456789'
# print(name[2])
# print(name[3])
# print(name[0])
# print(name[5])
# print(name[7])
# print(name[9])

# print(name[:5])
# print(name[:-1])
# print(name[-2:8:2])
# print(name[::-1])
# print(name[-1:-2:-1])
# mystr = 'what do you want from me,what do you do?'
# print(mystr.find('and'))
# print(mystr.find('do'))
# print(mystr.index('do'))
# print(mystr.index('you'))
# print(mystr.index('you'),0,30)
# print(mystr.rindex('me'))
# print(mystr.count('want',0,20))
# print(mystr.count('what'))
# print(mystr.replace('do','he'))
# print(mystr.replace('he','do'))
# print(mystr.replace('do','he',2))
# print(mystr.split('do'))
# print(mystr.split('do',2))
# print(mystr.split('you',-1))
# print(mystr.split('you'))
# mystr = ['what','do','you','want','from','me','?','what','do','you','do','?']
# print(' '.join(mystr))
'''
练习;
从键盘输入一个姓名，判断是否再班级内
如果在，则判断这个人在该班级内是否有重名得同学，
如果有有重名则输出重名得个数
如果不在，则提示不在
'''
# banji = "'zml','sunxue','wangtao','sunxue','pengpeng','xinxin'"
# name_list = ['lili','tom','xiaozhang','xiaowang','lisi','lisi']
# name = input('请输入您要搜索的名字：')
# if name in name_list:
#     print(f'您输入的名字是{name}，名字已经存在')
# else:
#     print(f'您输入的名字是{name}，名字不存在')
name_list = ['tom','lili','rose']
# name_list.append('ximengyao')
# print(name_list)
# name_list.append(['hesui,liuwen'])
# print(name_list)
# name_list.extend('hesui')
# print(name_list)
# del name_list
# print(name_list)
# del name_list[1]
# print(name_list)
# del_name = name_list.pop(1)
# print(del_name)
# print(name_list)
# name_list.remove('lili')
# print(name_list)
# name_list.clear()
# print(name_list)
# name_list[0] = 'ximengyao'
# print(name_list)
# name_list = [1,5,3,6,8,0,9]
# name_list.reverse()
# print(name_list)
# name_list.sort()
# print(name_list)
# name_list.sort(reverse = True)
# print(name_list)
# name_list2 = name_list.copy()
# print(name_list2)
# name_list = ['tom','lili','rose']
# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1
# for i in name_list:
#     print(i)

# name_list = [['小明','小红','小兰'],['tom','lili','rose'],['1','2','3']]
# print(name_list[0])
# print(name_list[0][1])
# name_list = ['第一',[第二],[第三]]
# teachers = [1,2,3,4,5,6,7,8]
# for name_list in teachers:
#     name_list1 = random.randit(0,2)
#     name_list[name_list1].append(name)
t1 = (10,)
print(type(t1))
t2 = (20)
print(type(t2))
t3 = ('hello')
print(type(t3))
tuple1 = ('a','b','c','d')
print(tuple1.index('a'))
print(tuple1[0])
print(tuple1.count('b'))
print(len(tuple1))
# tuple1[0] = 'aaa'
tuple2 = ('0','1',['11','22','33'],'4')
print(tuple2[2])
tuple2[2][1] = '222'
print(tuple2)
print(tuple2[2])
























