'''
算数运算符：
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

# 多个变量赋值
num1,str1,float1 = 10,'10',0.5
print(num1,str1,float1)

# 多变量赋相同值
a1 = b = 10
print(a1)
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
b *= 3
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
mystr = "hello world and superctest and chaoge and python"
print(mystr.find('and'))
print(mystr.find('and',15,30))



