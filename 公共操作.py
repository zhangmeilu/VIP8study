# 运算符
'''
+    合并---->字符串，列表，元组
*    复制---->字符串，列表，元组
in   元素是否存在---->字符串，列表，元组，字典
not in   元素是否不存在---->字符串，列表，元组，字典
'''

# +
str1 = 'a'
str2 = 'b'
str3 = str1 + str2
print(str3)

list1 = [1,2]
list2 = [3,4]
list3 = list1 + list2
print(list3)

t1 = (1,2)
t2 = (3,)
t3 = t1 + t2
print(t3)
# *
# 1.字符串
print('.' * 10)
# 列表
list1 = ['hello']
print(list1 * 4)
# 3.元组
t1 = ('world',)
print(t1 * 4)

# in 或 not in
# 1.字符串
print('a' in 'abcd')
print('a' not in 'abcd')
# 2.列表
list1 = ['a','b','c','d']
print('a' in list1)
print('a' not in list1)
# 3.元组
t1 = ('a','b','c','d')
print('a' not in t1)
print('aa' not in t1)
# 公共方法
'''
len()----->计算容器中元素个数
del 或 del()----->删除
max()----->返回容器中元素最大值
min()----->返回容器中元素最小值
range(start,end,step)----->生成从start到end的数字，步长为step，供for循环使用
enumerate()----->函数用于将一个可遍历的数据对象（如列表，元组，字符串）组合为一个索引序列
  同时列出数据和数据下标，一般用在for循环当中
'''
# len()
# 1.字符串
str1 = 'abcdefg'
print(len(str1))
list1 = [1,2,3,4]
print(len(list1))
t1 = [1,]
print(len(t1))
s1 = {}
print(len(s1))
dict1 = {'name' : 'zml','age' : 30}
print(len(dict1))
# del()
# 1.字符串
# str1 = 'abcdfeg'
# del str1
# print(str1)
# 2.列表
list1 = [10,20,30]
del (list1[1])
print(list1)
# max()
# 1.字符串
str1 = 'abcde'
print(max(str1))
# 2.列表
list1 = [10,20,30]
print(max(list1))
# min()
str1 = 'abcde'
print(min(str1))
list1 = [10,20,30]
print(min(list1))
# range()
# 1 2 3 4 5 6 7 8 9
for i in range(1,10,2):
    print(i)
for i in range(1,10,10):
    print(i)
for i in range(10):
    print(i)
# enumerate()
# 语法：enumerate(可遍历对象,start=0)
list1 = ['a','b','c','d','e']
for i in enumerate(list1):
    print(i)
for index,char in enumerate(list1,start=1):
    print(f'下标是{index},对应的字符是{char}')
# 三，容器类型转换
# tuple()
# 作用:将某个序列转换成元组
list1 = [10,20,30]
s1 = {10,20,30,40}
print(tuple(list1))
print(tuple(s1))

# list()
# 作用：将某个序列转换成列表
t1 = ('a','b','c','d','e','f')
s1 = {10,20,30,40}
print(list(t1))
print(list(s1))

# set()
# 将某个序列转换成集合
list1 = ['a','b','c','d','e','f']
t1 = (10,20,30)
print(set(list1))
print(set(t1))















































