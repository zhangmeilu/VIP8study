# try:
#     f = open('test.txt','r')
# except:
#     f = open('test.txt','w')
# try:
#     print(1/0)
# except(NameError,ZeroDivisionError):
#     print('有错误')
# try:
#     print(num)
# except (NameError,ZeroDivisionError) as result:
#     print(result)
# try:
#     print(num)
# except Exception as result:
#     print(result)
# try:
#     print(1)
# except Exception as result:
#     print(result)
# else:
#     print('...')
try:
    f = open('test.txt','r')
except Exception as result:
    f = open('test.txt','w')
else:
    print('无异常')
finally:
    print('进程结束')





















