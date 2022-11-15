from math import ceil
a = input('Введите строку: ')
b = ceil(len(a) / 2)
print(a[b:], a[:b], sep='')
