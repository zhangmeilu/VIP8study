# 元组
t1 = (10,20,30)
t2 = (10,)
print(type(t2))
t3 = (10)
t4 = ('10')
print(type(t3))
print(type(t4))
# 元组不支持修改，只能查找
tuple1 = ('a','b','c','b')
print(tuple1[0])
print(tuple1.index('a'))
# print(tuple1.index('e'))
print(tuple1.count('b'))
print(len(tuple1))
# tuple1[0] = 'aa'
tuple2 = (10,20,['a','b','c'],30,40)
print(tuple2[2])
tuple2[2][0] = 'aa'
print(tuple2[2][0])

































































