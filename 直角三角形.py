a = '******'
for i in a:
    print(a[:-1])
    a = a[:-1]

j = 1
while j <= 5:
    i = 1
    while i <= j:
        print('*',end='\t')
        i += 1
    print()
    j += 1



