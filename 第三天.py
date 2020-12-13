# def sum_num(a,b,c):
#     return a + b + c
# print(sum_num(1,2,3))
# def avg_num(a,b,c):
#     return(a + b + c)/3
#     result(avg_num())
# print(avg_num(1,2,3))

# def testA():
#     a = 100
#     print(a)
# testA()
# print(a)
# 定义一个全局变量a
# a = 100
# def testA():
#     print(a)
# def testB():
#     print(a)
# testA()
# testB()
# 思考：testB函数希求修改变量a的值为200，如何修改程序？
# a = 100
# def testA():
#     print(a)
# def testB():
#     a = 200
#     print(a)
# testA()
# testB()
# print(f'全局变量a = {a}')

# 思考：如何再函数体内部修改全局变量？
# 使用global声明这个变量为全局变量
# a = 100
# def testA():
#     print(a)
# def testB():
#     global a
#     a = 200
#     print(a)
# testA()
# testB()
# print(f'全局变量a = {a}')

# 多函数程序执行流程
# glo_num = 0
# def test1():
#     global glo_num
#     glo_num = 100
# def test2():
#     print(glo_num)
# test1()
# test2()

# def user_info(name,age,gender):
#     print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
# user_info('rose',age=20,gender='女')
# user_info('Tom',20,'男')

# def user_info(name,age,gender='男'):
#     print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
# user_info('Tom',20)
# user_info('rose',18,'女')
# def user_info(*args):
#     print(args)
# user_info('Tom')
# user_info('Tom',18)
# list1 = [1,2,3]
# user_info(*list1)
#
# def user_info(**kwargs):
#     print(kwargs)
# user_info(name='Tom',age=18,id=110)
# dict1={'name':'Tom','age':18,'id':110}
# user_info(**dict1)

# 拆包：元组
def return_num():
    return 100,200
num1,num2 = return_num()
print(num1)
print(num2)
# 拆包：字典
dict1 = {'name':'Tom','age':18}
a,b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])

def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))
# int:计算前后id值不同
b=100
test1(b)
# 列表：计算前后id值相同
c = [11,22]
test1(c)











































