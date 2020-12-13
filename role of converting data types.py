'''
num = input('请输入数字：')
print(f'数字是{num}')
print(type(num))
print(type(int(num)))
'''

num1 = 1
print(float(num1))
print(type(float(num1)))

num2 = 10
print(str(num2))
print(type(str(num2)))

list1 = [10,20,30]
print(tuple(list1))
print(type(tuple(list1)))

t1 = (100,200,300)
print(list(t1))
print(type(list(t1)))

str1 = '10'
str2 = '[1,2,3]'
str3 = '{10,20,30}'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))