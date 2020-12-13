# 注释的作用:能够大大增强此程序的可读性
# 注释分为单行注释和多行注释
# 多行注释的方法:
'''
# 注释内容
'''
"""
# 注释内容
"""
# 或:
# 全选一段代码,按ctrl+/

# 变量就是一个存储数据的时候当前数据所在的内存地址的名字而已
# 定义变量:
# 变量名 = 值
'''
标识符：
1.由数字、字母、下划线组成
2.不能数字开头
3.不能使用内置关键字
4.严格区分大小写
'''
'''
命名习惯：
1.见名知义
2.大驼峰：即每个单词首字母都大写，例如：MyName
3.小驼峰：第二个（含）以后的单词首字母大写，例如：myName
4.下划线：例如：my_name
'''
# 使用变量
my_name = 'zml'
print(my_name)

# 认识数据类型
'''
数据类型：
1.数值：int（整型）、float（浮点型）
2.布尔型：true（真）、false（假）
3.str（字符串）
4.list(列表)
5.tuple（元组）
6.set（集合）
7.dict（字典）
'''
# 检测数据类型的方法：
a = 1
print(type(a))
b = 0.1
print(type(b))
c = '你好'
print(type(c))
d = (1,2,3)
print(type(d))
e = [10,20,30]
print(type(e))
f = {100,200,300}
print(type(f))
g = {'name':'zml','age':20}
print(type(g))

# 输出：
'''
格式化输出：
        1.格式化符号
        2.f-字符串
    print的结束符
'''
age = 18
print('age')
age1 = 18
print(age1)

# 格式化符号
'''
目前用到的：
%s----字符串
%d----有符号的十进制整数
%f----浮点数
'''
'''
%06d----表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出
%.2f----表示小数点后显示的小数位数
'''
# 例：格式化字符串除了%s，还可以写成f'表达式}'
age = 18
name = 'zml'
weight = 62.5
student_id = 1
print('我的名字是%s' % name)
print('我的学号是%04d' % student_id )
print('我的体重是%.2f' % weight)
print('我的名字是%s,今年%d岁了' % (name,age))
print('我的名字是%s,明年%d岁了' % (name,age+1))
print(f'我的名字是{name},明年{age+1}岁了')
# 转义字符
'''
1.\n----换行
2.\t----制表符，一个tab（4个空格）的距离
'''
# print结束符
# print('内容',end="")

# 输入：
# 输入的语法；input("提示信息")
# 当程序执行到input，等待用户输入，输入完成之后才继续向下执行
'''
password = input("请输入密码：")
print(f'您输入的密码:{password}')
print(type(password))
'''
# 转换数据类型的函数
'''
int(x,[base])----将x转换为一个整数
float(x)----将x转换为一个浮点数
str(x)----将x转换为一个字符串类型
eval(str)----用来计算在字符串中的有效python表达式，并返回一个对象
tuple(s)----将序列s转换为一个元组
list(s)----将序列s转换为一个列表
'''
'''
num = input("请输入您的幸运数字：")
print(f'您的幸运数字是{num}')
print(type(num))
print(type(int(num)))
'''
# 1.float()----转换成浮点型
num = 1
print(float(num))
print(type(float(num)))

# 2.str()----转换成字符串类型
num1 = 10
print(str(num1))
print(type(str(num1)))

# 3.tuple()----讲一个序列转换成元组
num2 = [10,20,30]
print(tuple(num2))
print(type(tuple(num2)))

# 4.list()----讲一个序列转换成列表
num3 = [100,200,300]
print(list(num3))
print(type(list(num3)))

# 5.eval()----将字符串中的数据转换成python表达式原本类型
str1 = '10'
str2 = '[1,2,3]'
str3 = '{10,20,30}'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

# 运算符的分类
'''
    +   加
    -   减
    *   乘
    /   除
    //  整除
    %   取余
    **  指数  ----几次方
    ()  小括号 ---提高运算优先级
注意：混合运算优先级顺序：（）高于**高于/ // %高于 + -
'''
'''
赋值运算符：
    =   赋值  将=右侧的结果赋值给等号左边的变量

'''

# 单个变量赋值
num = 1
print(num)
#多个变量赋值
num1,float1,str1 = 10,0.5,'你好'
print(num1)
print(float1)
print(str1)

# 多变量赋相同值
a = b = 2
print(a)
print(b)

# 复合赋值运算符
#     +=   加法赋值运算符  c += a 等价于 c= c+a
#     -=   减法赋值运算符  c -= a 等价于 c=c-a
#     *=   乘法赋值运算符  c *= a 等价于 c=c*a
#     /=   除法赋值运算符  c /= a 等价于 c=c/a
#     //=  整除赋值运算符  c //= a 等价于 c=c//a
#     %=   取余赋值运算符  c %= a 等价于 c=c%a
#     **=  幂赋值运算符    c **= a   等价于  c= c**a
a = 100
a += 1
print(a)
b = 2
b -= 1
print(b)
c = 10
c += 1 + 2
print(c)

# 比较运算符
#   ==  判断相等
#   !=  不等于

a = 7
b = 5
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

# 逻辑运算符
#   and     x and y  ---布尔：与，其中一个是假，那么返回就是假
#   or      x or y ---布尔：或，其中一个是假，那么返回就是真
#   not     not x  ---布尔：非，若x为真，返回就是假，反之则相反

a = 1
b = 2
c = 3
print((a < b)and(b > a))
print((a > b)and(b < a))
print((a < b)and(b > a))
print((a < b)or(b > c))
print(not (a > b))
print(not (b > c))
print(not (b < c))

# 拓展
#   数字之间的逻辑运算
a = 0
b = 1
c = 2
print(a and b)
print(b and c)
print(b or a)
print(a or c)
print(a and c)
print(b or c)
print(a and a)
print(a or a)

# 字符串输入
'''
name = input('请输入您的名字：')
print(f'您输入的名字是{name}')
print(type(name))

password1 = input('请输入您的密码：')
print(f'您输入的密码是{password1}')
print(type(password1))
'''
# 索引/下标：下标是从0开始
'''
name = "123456"
print(name[1])
print(name[0])
print(name[4])
'''
'''
name = "qwertyuiop"
print(name[1:2])
print(name[2:5:2])
print(name[:-1])
print(name[:-5])
print(name[::-1])
'''
# mystr = "hello world and superctest and chaoge and python"
# print(mystr.find('and'))
# print(mystr.find('and',15,30))

# if 语法：
'''
if 条件：
    条件成立执行的代码1
    条件成立执行的代码2
    ......
'''
# if True:
#     print('条件成立执行的代码1')
#     print('条件成立执行的代码2')
# print('我是无论条件是否成立都要执行的代码')

# 需求：如果用户年龄大于18岁，即成年，输出"已经成年，可以上网"
# age = 20
# if age >= 18:
#     print(f'已经承诺，可以上网')
# print('系统关闭')

# 进阶版
# 需求：用户可以输出自己的年龄，然后系统进行判断是否成年，成年则输出"您的年龄是'用户输入的年龄',已经成年，可以上网"
# age = int(input('请输入您的年龄：'))
# if age >= 18:
#     print('您的年龄是%d' % age)
#     print("已经成年，可以上网")
#   第296行代码若不加int，最后则提示：TypeError: '>=' not supported between instances of 'str' and 'int'。

# if...else

# 语法：
'''
    if 条件：
        条件成立执行的代码1
        条件成立执行的代码2
        ...
    else:
        条件不成立执行的代码1
        条件不成立执行的代码2
        ...
'''
# 需求；网吧上网的实例，如果成年，允许上网，如果不承诺，提示不能上网，回家学习
'''
age = int(input("请输入您的年龄："))
if age >= 18:
    print(f'您的年龄是%d' % age,'可以上网')
else:
    print("不许上网，回家写作业")
print("系统关闭")
'''
# 中国合法工作年龄为18-60岁，即如果年龄小于18的情况下为童工，不合法；如果年龄在18-60之间为合法年龄；大于60岁为法定退休年龄
'''
if 条件1：
    条件1成立执行的代码1
    条件1成立执行的代码2
    ...
elif 条件2：
    条件2成立执行的代码1
    条件2成立执行的代码2
    ...
else:
    以上条件都不成立执行的代码
'''
'''
age = int(input('请输入您的年龄：'))
if age < 18:
    print("违法雇佣童工")
elif 18<= age <= 60:
    print("合法工龄")
else :
    print("该退休啦")
'''
# if 嵌套
# 思考：坐公交：如果有钱可以上车，没钱不能上车；上车后如果有座，则可以坐下，如果没座，就要站着
'''
 if 条件1：
    条件1成立执行的代码
    条件1成立执行的代码
    
    if 条件2：
        条件2成立执行的代码
        条件2成立执行的代码
'''
# money = 1---有钱
# poor = 0---没钱
'''
seat = 0
money = 1
if money == 1:
    print("可以上车")
    if seat == 1:
        print("坐下")
    else:
        print("站着")
else:
    print("不许上车")
'''

# while 的语法：
'''
while 条件：
    条件成立重复执行的代码1
    条件成立重复执行的代码2
    ...
'''
# 重复写5遍：我错了
'''
i = 0
while i < 5:
    print("我错了")
    i += 1
print("结束")
'''
# 计算1-100累加和
i = 0
result = 0
while i <= 100:
    result += i
    i += 1
    print(result)
# 计算1-100偶数累加和
i = 0
result = 0
while i <= 100:
    result += i
    i += 2
    print(result)
# break and continue
# i = 1
# while i <= 5:
#     if i == 4:
#         print(f'吃饱了不吃了')
#         break
#     print(f'吃了第{i}个苹果')
#     i+= 1
# i = 1
# while i <= 5:
#     if i == 3:
#         print(f'大虫子，第{i}个不吃了')
#         i+= 1
#         continue
#     print(f'吃了第{i}个苹果')
#     i += 1


# while 条件:
#     print('媳妇儿，我错了')
# print('刷碗')

# j = 0
# while j < 3:
#     i = 0
#     while i < 3:
#         print('我错了')
#         i += 1
#     print('刷碗')
#     print('结束')
#     j += 1


#    作业一：（直角三角形）
# （第一种）：
j = 1
while j <= 5:
    i = 1
    while i <= j:
        print('*',end='\t')
        i += 1
    print()
    j += 1

#  （第二种）：
a = '******'
for i in a:
    print(a[:-1])
    a = a[:-1]

# 作业二：（乘法表）
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i*j}',end='\t')
        i += 1
    print()
    j += 1

# 其他的作业不会了。有答案的没看懂




















































