# 数据类型
# 变量名自定义，要满足==标识符==命名规则
'''
由数字，字母，下划线组成
不能数字开头
不能使用内置关键字
严格区分大小写
'''
# 命名习惯
'''
见名之义
大驼峰：每个单词首字母都大写，例如：MyName
小驼峰：除首字母外，第二个（含）以后得单词首字母大写，例如：myName
下划线：例如：my_name
'''
# 认识数据类型
'''
数值：整数，浮点数
# 字符串:str
布尔型：True/False
列表：list
元组：tuple
集合:set
字典:dict
'''
a = 1
print(type(a))
b = 0.1
print(type(b))
c = 'hello'
print(type(c))
d = [1,2]
print(type(d))
e = (1,)
print(type(e))
f = {1,2,3}
print(type(f))
g = True
print(type(g))
h = {'name': 'Tom','age':18}
print(type(h))
# 输出：我的年龄18岁
age = 18
print(age)
# 格式化输出
'''
%s: 字符串
%d: 有符号得十进制整数
%f：浮点数
%06d：表示输出得整数显示位数，不足以0补全，超出当前位数则原样输出
%.2f：表示小数点后显示得小数位数
'''
# 代码示范
# 格式化字符串除了%s，还可以写为f'{表达式}'
age = 18
name = 'zml'
weight = 75.5
sid = 1
print("age=%d" % age)
print("name=%s" % name)
print("weight=%.2f" % weight)
print("age=%d,name=%s,weight=%.2f" % (age,name,weight))
print("age=%s,name=%s,weight=%s" % (age,name,weight))
# \n,\t,表示换行和tab
print(f"\tage={age},\n\tname={name},\n\tweight={weight}")
# 结束符
# print("输出得内容：hello",end="\n")

# 四，输入
# 在python中，程序接收用户的数据的功能即是输入
# 语法：
# input("提示信息")
# 特点：
'''
1.当程序执行到input，等待用户输入，输入完后才继续向下执行
2.在python中，input接收用户输入后，一般存储到变量，方便使用
3.在python中，input会把接收到的任意用户输入的数据都当作字符串处理
'''
# password = input('请输入您的密码：')
# print(f'您输入的密码是{password}')
# print(type(password))

# 五，数据类型的转换
'''
int(x[,base])   ---    将x转换成一个整数
float(x)        ---    将x转换成一个浮点数
str(x)          ---    将x转换成字符串
eval(str)       ---    用来计算在字符串中的有效python表达式，并返回一个对象
tuple(s)        ---    将序列s转换为一个元组
list(s)         ---    将序列s转换为一个列表
'''
# 接收用户输入：
num = input("请输入您的密码：")
# 打印结果
print(f"您输入的密码是{num}")
# 检测用户输入的数据类型
print(type(num))
# 转化数据类型为整形
print(type(int(num)))
# 六，运算符
'''
1.算数运算符
2.赋值运算符
3.复合赋值运算符
4.比较运算符
5.逻辑运算符
'''
# 算数运算符









































































































































































































