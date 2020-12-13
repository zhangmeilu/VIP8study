# 3 + 2 + 1
# def sum_numbers(num):
#     # 1.如果是1，直接返回1  --出口
#     if num == 1:
#         return 1
# #     2.如果不是1，重复执行累加并返回结果
#     return num + sum_numbers(num-1)
# sum_result = sum_numbers(3)
# print(sum_result)



# def fn1():
#     return 200
# print(fn1)
# print(fn1())
# # lambda表达式
# fn2 = lambda : 100
# print(fn2)
# print(fn2())

# def add(a,b):
#     return a + b
# result = add(1,2)
# print(result)

# lambds表达式
# fn1 = lambda a,b: a + b
# print(fn1(2,3))
#
# fn1 = lambda a,b:a if a > b else b
# print(fn1(400,500))
#
# students = [
#     {'name':'Tom','age':20},
#     {'name':'rose','age':19},
#     {'name':'jack','age':21}
# ]
# students.sort(key=lambda x:x['name'])
# print(students.sort(key=lambda x:x['name'],reverse=True))
# print(students)
# students.sort(key=lambda x: ['age'])
# print(students)
# def sum_num(a,b,f):
#     return f(a) + f(b)
# result = round(-1,2)
# print(result)

# list1 = [0,2,4,6,8,10]
# def func(x):
#     return x ** 3
# result = map(func,list1)
# print(result)
# print(list(result))

import functools
list1 = [0,2,4,6,8,10]
def func(a,b):
    return a + b
result = functools.reduce(func,list1)
print(result)

















