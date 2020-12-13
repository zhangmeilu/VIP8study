# 循环的作用：让代码更高效的重复执行
# 在python 中，循环分为while 和 for两种，最终实现效果相同
# while的语法
# 需求：复现重复执行100次print('媳妇儿，我错了')
# i = 0
# while i < 101:
#     print('媳妇儿，我错了')
#     i += 1
# print('任务结束')

# while 的应用
# 计算1-100累加和
# i = 0
# result = 0
# while i <= 100:
#     result += i
#     i += 1
# print(result)

# 计算1-100偶数累加和
# i = 1
# result = 0
# while i <= 100:
#     result += i
#     i += 2
# print(result)
# break and continue
# i = 1
# while i <= 5:
#     if i == 4:
#         print("吃饱了")
#         break
#     print(f'吃了第{i}个苹果')
#     i += 1
# i = 1
# while i <= 5:
#     if i == 3:
#        print(f'吃到大虫子，第{i}个不吃了')
#        i += 1
#        continue
#     print(f'吃了第{i}个苹果')
#     i += 1
#
# 五，while循环嵌套
# j = 0
# while j < 3:
#     i = 0
#     while i < 3:
#         print('我错了')
#         i += 1
#     print('刷碗')
#     j += 1
#      print('结束')
# j = 1
# while j <= 5:
#     i = 1
#     while i <= j:
#         print('*',end='\t')
#         i += 1
#     print()
#     j += 1
#
# j是行数，i是个数
# a = ['*','*','*','*','*']

# a = '*****'
# for i in a:
#     print(a[5::-1])
#     a = a[5::-1]

# a = '******'
# for i in a:
#     print(a[5:0:-1])
#     a = a[5:0:-1]

# a = "******"
# print(a[:-1])
# print(a[:-2])
# print(a[:-3])
# print(a[:-4])
# print(a[:-5])
# print(a[:1])
# print(a[:2])
# print(a[:3])
# print(a[:4])
# print(a[:5])































