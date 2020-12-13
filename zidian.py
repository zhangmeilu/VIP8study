# 创建字典的方法
# 字典为大括号
# 数据为"键值对"形式出现
# 各个'键值对'之间用'逗号'隔开
# 有数据字典
dict1 = {'name': 'zml','age':20,'gender':'男','weight': 69.5}
# 空字典
dict2 = {}
dict3 = dict()
# 字典常见操作
# 增
# 写法：字典序列[key] = 值
# dict1 = {'name': 'zml','age':20,'gender':'男','weight': 69.5}
# dict1['name'] = 'zyc'
# print(dict1)
# dict1['id'] = 110
# print(dict1)
# 删
dict1 = {'name': 'zml','age': 20,'gender': '男'}
del dict1['gender']
print(dict1)
# 清空字典
dict1 = {'name': 'zml','age':20,'gender':'男','weight': 69.5}
dict1.clear()
print(dict1)
# 改
# 查
# key值查找
dict1 = {'name': 'zml','age':20,'gender':'男','weight': 69.5}
print(dict1['name'])
# print(dict1['id'])
# get()
# 语法：字典序列.get(key,默认值)
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.get('name'))
print(dict1.get('id,110'))
print(dict1.get('id'))
# keys()
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.keys())
# values()
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.values())
# items()
dict1 = {'name':'Tom','age':20,'gender':'男'}
print(dict1.items())
# 字典的循环遍历
dict1 = {'name':'Tom','age':20,'gender':'男'}
for key in dict1.keys():
    print(key)

# 遍历字典的value
dict1 = {'name':'Tom','age':20,'gender':'男'}
for value in dict1.values():
    print(value)

# 遍历字典的元素
dict1 = {'name':'Tom','age':20,'gender':'男'}
for item in dict1.items():
    print(item)
# 遍历字典的键值对
dict1 = {'name':'Tom','age':20,'gender':'男'}
for key,value in dict1.items():
    print(f'{key} : {value}')



























