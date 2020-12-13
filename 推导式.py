# 作用：用一个表达式创建一个有规律的列表或控制一个有规律的列表
# 列表推导式又叫列表生成式
# 需求：创建一个0-10的列表
# while循环实现
from homework import num

list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# for循环实现
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# 带if的列表推导式
# 需求：创建0-10的偶数列表
# 方法一：range()步长实现
list1 = [i for i in range(0,10,2)]
print(list1)

list2 = [i for i in range(1,10,2)]
print(list2)

# 方法2：if实现
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)
list2 = [i for i in range(10) if i % 2 == 1]
print(list2)

# 多个for循环实现列表推导式
# 需求：创建列表如下：
# [(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
list1 = [(i,j) for i in range(1,3) for j in range(3)]
print(list1)

# 字典推导式
# 思考：如果有如下两个列表：
# list1 = ['name','age','gender']
# list2 = ['Tom',20,'男']
# 如何快速合并为一个字典：字典推导式
# 创建一个字典：字典key是1-5数字，value是这个数字的2次方
dict1 = {i: i**2 for i in range(1,5)}
print(dict1)

# 将两个列表合并为一个字典
list1 = ['name','age','gender']
list2 = ['Tom',20,'男']
dict1 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict1)

# 提取字典中目标数据
counts = {'MBP': 268,'HP': 125,'DELL': 201,'Lenovo': 199,'acer': 99}
count1 = {key: value for key,value in counts.items() if value <= 200}
print(count1)

# 集合推导式
# 需求：创建一个集合，数据为下方列表的2次方
# list1 = [1,1,2]
# set1 = {i ** 2 for i in list1}
# print(set1)


# password = input('请输入密码： ')
# print(f'您输入得密码是：{password}')
# print(type(password))
#
# num = input('请您输入您的幸运数字：')
# print(f"您的幸运数字是{num}")
# print(type(num))
# print(type(int(num)))
# mystr = "hello"
# print(mystr.split(' ',5))

# mystr = ['h','e','l','l','o']
# print(''.join(mystr))

mystr = "hello world and you"
print(mystr.lstrip('h'))


# list1 = [1,2,3,4,5,5,2,3,4,2,4]
# print(set(list1))
# 思考：坐公交：如果有钱可以上⻋，没钱不能上⻋；上⻋后如果有空座，则可以坐下；如果没空座，就要站着。怎么书写程序？
# money = 1表示有钱，money = 0表示没钱
# seat = 0表示没座，seat = 1 表示有座
# money = 1
# # seat = 0
# # input('请投币：')
# # input('是否有座位： ')
# # if money == 1:
# #     print('请上车')
# #     if seat == 1:
# #         print('有空位，请坐')
# #     else:
# #         print('请站稳扶好')
# # else:
# #     print('余额不足，请充值，不得上车')
# money = 1
# seat = 0
# if money == 1:
#     print('⼟豪，不差钱，顺利上⻋')
#     if seat == 1:
#         print('有空座，可以坐下')
#     else:
#         print('没有空座，站等')
# else:
#     print('没钱，不能上⻋，追着公交⻋跑')
# import random
# random.randint()
#
# a = 1
# b = 2
# c = a if a > b else b
# print(c)
# list1 = [i for i in range(100) if i % 3 == 0]
# print(list1)
# list1 = [i for i in range(0,100,3)]
# print(list1)

# list1 = [3,2,1,5,4,0,2]
# for i in list1:
#     i = i ** 2
#     print(list1)
# list1 = [3,2,1,5,4,0,2]
# set1 = {1 ** 2 for i in list1}
# print(set1)
#
# list1 = ['name']
# list2 = ['Tom']
# list3 = list1 + list2
# print(list3)
# print(dict{list3})

# 3 + 2 + 1
# def sum_numbers(num):
#     if num == 1:
#         return 1
#     return num + sum_numbers(num - 1)
# sum_result = sum_numbers(4)
# print(sum_result)
# 1,1,2,3,5,8,11,19...
# def sum_numbers(num):
#     if num == 1:
#         return 1

# list1 = [1,2,3,4,5,5,2,3,2,4]
# print(set(list1))


# list1 = [i for i in range(100) if i % 3 == 0]
# print(list1)



































