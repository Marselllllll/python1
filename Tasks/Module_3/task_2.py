a=input('Введите строку: ')
a1=a.find(' ')
a2=a1+1
print(str(a[a2:]) + ' ' + str(a[:a1]))