# 查找
# find():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.find('and'))
print(mystr.find('and', 15, 30))
print(mystr.find('ands'))
# index():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.index('and'))
print(mystr.index('and', 15, 30))
# print(mystr.index('ands'))
# rfind():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.rfind('and'))
print(mystr.rfind('and', 15, 30))
print(mystr.rfind('ands'))
# rindex():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.rindex('and'))
print(mystr.rindex('and', 15, 30))
# print(mystr.rindex('ands'))
# count():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.count('and'))
print(mystr.count('and', 15, 30))
print(mystr.count('ands'))
# 修改
# replace():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.replace('and', 'he'))
print(mystr.replace('and', 'he', 1))
print(mystr)
# split():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.split('and'))
print(mystr.split('and', 2))
print(mystr.split(' '))
print(mystr.split(' ', 2))
# join():
list = ['chao', 'ge', 'that', 'promotion']
t1 = ('aa', 'b', 'cc', 'ddd')
print(' '.join(list))
print('...'.join(t1))
# capitalize():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.capitalize())
# title():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.title())
# lower():
mystr = "Hello World And Superctest And Chaoge And Python"
print(mystr.lower())
# upper():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.upper())
# lstrip():
mystr = "  hello world and superctest and chaoge and Python"
print(mystr.lstrip())
# rstrip():
mystr = "hello world and superctest and chaoge and Python   "
print(mystr.rstrip())
# strip():
mystr = " hello world and superctest and chaoge and Python "
print(mystr.strip())
# ljust():
mystr1 = "hello"
print(mystr1.ljust(20, '*'))
print(mystr1.ljust(10))
# rjust():
mystr2 = 'hello'
print(mystr2.rjust(10))
print(mystr2.rjust(10, '.'))
# center():
mystr3 = 'hello'
print(mystr3.center(10))
print(mystr3.center(10, '.'))
# 判断
# startswith():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.startswith('and', 15, 30))
print(mystr.startswith('hello'))
# endswith():
mystr = "hello world and superctest and chaoge and Python"
print(mystr.endswith('hello'))
print(mystr.endswith('Python'))
print(mystr.endswith('Python', 5, 30))
# isalpha():
mystr1 = 'hello'
mystr2 = '123abc'
print(mystr1.isalpha())
print(mystr2.isalpha())
# isdigit():
mystr1 = '123456'
mystr2 = '111aaa'
print(mystr1.isdigit())
print(mystr2.isdigit())
# isalnum():
mystr1 = '123456-'
mystr2 = 'aaa123'
print(mystr1.isalnum())
print(mystr2.isalnum())
# isspace():
mystr = ' '
mystr1 = '123 '
print(mystr.isspace())
print(mystr1.isspace())

# 列表：
# 查找：1.下标
# name_list = ['Tom','Lily','Rose']
# print(name_list[0])
# print(name_list[2])
# print(name_list[1])
# print(name_list[-1])
# index():
name_list = ['Tom', 'Lily', 'Rose']
print(name_list.index('Tom', 0, 2))
print(name_list.index('Lily', 0, 2))
# count():
name_list = ['Tom', 'Lily', 'Lily', 'Rose']
print(name_list.count('Lily'))
# len():
name_list = ['Tom', 'Lily', 'Lily', 'Rose']
print(len(name_list))
# 判断是否存在:in
name_list = ['Tom', 'Lily', 'Lily', 'Rose']
print('Lily' in name_list)
print('xiaozhan' in name_list)
# not in
name_list = ['Tom', 'Lily', 'Lily', 'Rose']
print('xiaozhan' not in name_list)
print('Lily' not in name_list)

# 需求：查找用户输入的名字是否已经存在
# name_list = ['Tom','Lily','Rose']
# name = input('请输入您要搜索的名字： ')
# if name in name_list:
#     print(f'您输入的名字是{name}，名字已经存在')
# else:
#     print(f'您输入的名字是{name}，名字不存在')
# append():
# name_list = ['Tom','Lily','Rose']
# name_list.append('xiaozhan')
# print(name_list)
# name_list = ['Tom','Lily','Rose']
# name_list.append(['xiaozhan','wangyibo'])
# print(name_list)

# extend():
# name_list = ['Tom','Lily','Rose']
# name_list.extend('xiaozhan')
# print(name_list)
# name_list = ['Tom','Lily','Rose']
# name_list.extend(['xiaozhan','wangyibo'])
# print(name_list)
# # insert():
# name_list = ['Tom','Lily','Rose']
# name_list.insert(2,'xiaozhan')
# print(name_list)
# name_list = ['Tom','Lily','Rose']
# name_list.insert(1,'xiaozhan')
# print(name_list)
# 删除
# name_list = ['Tom','Lily','Rose']
# del name_list
# print(name_list)
# del name_list[0]
# print(name_list)
# pop():
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.pop(1)
# print(name_list)
# # remove():
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.remove('Tom')
# print(name_list)
# # clear():
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.clear()
# print(name_list)
# # 修改
# name_list = ['Tom', 'Lily', 'Rose']
# name_list[0] = 'xiaozhan'
# print(name_list)
# # 逆置：reverse():
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.reverse()
# print(name_list)
# 排序：sort():
# 列表序列。sort(key= None,reverse=False)
# reverse= True是降序，reverse=Flase是升序
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.sort(reversed(False))
# print(name_list)
# name_list.sort(reverse=True)
# print(name_list)
# 复制
# copy()
# name_list = ['Tom', 'Lily', 'Rose']
# name_list2 = name_list.copy()
# print(name_list2)
# 四，列表的循环遍历
# 需求：依次打印列表中的各个数据
# while
# name_list = ['Tom', 'Lily', 'Rose']
# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1
# digit_list = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < len(digit_list,):12q
#     digit_list.sort(reverse= True)
#     print(digit_list[i])
#     i += 1
# digit_list = [1,2,3,4,3,4,2,5,5,8,9,7]
# digit_list2 = list(set(digit_list))
# i = 0
# while i < len(digit_list):
#     digit_list.sort(reverse=False)
#     print(digit_list[i])
#     i += 1
# for:
name_list = ['Tom','Lily','Rose']
for i in name_list:
    print(i)

# 五，列表嵌套
# 需求：要存储班级一二三个班级学生姓名，且每个班级的学生姓名在一个列表
name_list = [['小米','小美','小花'],['xiaozhan','wangyibo','chenqingling'],['Tom','Rose','Tina']]













































































































