a = input('Введите строку: ')
b1 = a.index('h')
b2 = a.rindex('h')
print(a[:b1], a[b2+1:], sep='')

# In the hole in the ground there lived a hobbit