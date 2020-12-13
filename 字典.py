# list1 = ['tom','男','20']
# print(list1[0])
# 空字典
# dict2 = {}
# dict3 = dict()
dict1 = {'name':'ximengyao', 'age':20, 'gender':'男'}
dict1['name'] = 'xiaozhan'
print(dict1)

dict1['id'] = 110
print(dict1)
# 删
dict1 = {'name': 'ximengyao', 'age': 20, 'gender': '男'}
del dict1['gender']
print(dict1)
dict1 = {'name':'ximengyao', 'age':20, 'gender':'男'}
dict1.clear()
print(dict1)
#
# 改

dict1 = {'name':'xiaozhan', 'age':20, 'gender':'男'}
s1 = {10,20,30,40,50}
print(s1)
s2 = {10,20,30,40,50,10,20,30}
print(s2)
s3 =set('qwert')
print(s3)
s4 = set()
print(type(s4))
s5 = {}
print(type(s5))
s6 = {10,20}
s6.add(100)
s6.add(10)
print(s6)
s6.update([100,200])
s6.update('qwe')
print(s6)
s6.remove(10)
print(s6)
s6.remove(10)
print(s6)
s6 = {10,20}
s6.discard(10)
print(s6)
s6.discard(10)
print(s6)
s1 = {10,20,30,40,50}
del_num = s1.pop()
print(del_num)
print(s1)
# 查找数据
print(10 in s1)
print(60 not in s1)
print(50 not in s1)















































