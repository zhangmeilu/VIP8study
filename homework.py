# 求100以内能被3整除的数，并将作为列表输出
list1 = [i for i in range(100) if i % 3 == 0]
print(list1)
list2 = [i for i in range(0,100,3)]
print(list2)

# 求100以内的质数（只能被1和它本身整除）
# list1 = [i for i in range(2,100) for j in range(2,i) if i % j == 0]
# print(list1)

num = []
i = 2
for i in range(2,100):
    j = 2
    for j in range(2,i):
        if (i % j == 0):
            break
    else:
        num.append(i)
print(num)

# 第四题：
# f(n) = f(n-1)+f(n-2)























































