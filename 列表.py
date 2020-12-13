# 下标：
# name_list = ['tom','lily','rose']
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])
# 函数
# 列表序列.index(数据，开始位置下标，结束位置下标)
# name_list = ['tom','lily','rose','hehe']
# print(name_list.index('hehe',0,3))
# count():统计指定数据在当前列表中出现的次数
name_list = ['tom','lily','rose','tom']
print(name_list.count('tom'))
# len():访问列表长度，即列表中数据的个数
name_list = ['tom','lily','rose','tom']
print(len(name_list))
# in:判断指定数据在魔偶个列表序列，如果在返回True，否则返回False
name_list = ['tom','lily','rose','tom']
print('lily' in name_list)
print('lilys' in name_list)
print('lily' not in name_list)
print('gege' not in name_list)


