# 集合
# 创建集合使用{}或set{}，但是如果要创建空集合只能使用set{}，因为{}用来创建空字典
s1 = {10,20,30,40,50}
print(s1)
s2 = {10,30,20,10,30,40,30,50}
print(s2)
s3 = set('abcdefg')
print(s3)
s4 = set()
print(type(s4))
s5 = {}
print(type(s5))
# 特点：
# 1.集合可以去重
# 2.集合数据是无序的，故不支持下标
# 二，集合常见的操作方法
# 增加数据
# add()
s1 = {10,20}
s1.add(100)
s1.add(10)
print(s1)
# update(),追加的数据是序列
s1 = {10,20}
# s1.update(100)
s1.update([100,200])
s1.update('abc')
print(s1)
# 删除数据
# remove(),删除集合中的指定数据，如果数据不存在则报错
s1 = {10,20}
s1.remove(10)
# print(s1)
# s1.remove(10)
print(s1)
# discard(),删除集合中的指定数据，如果数据不存在也不会报错
s1 = {10,20}
s1.discard(10)
print(s1)
s1.discard(10)
print(s1)
# pop(),随机删除集合中的某个数据，并返回这个数据
s1 = {10,20,30,40,50}
del_num = s1.pop()
print(del_num)
print(s1)
# 查找数据
# in: 判断数据在集合序列
# not in:判断数据不在集合序列
s1 = {10,20,30,40,50}
print(10 in s1)
print(60 not in s1)
print(10 not in s1)
































































