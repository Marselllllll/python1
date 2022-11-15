a = input('Введите строку: ')
b1 = a.index('h')
b2 = a.rindex('h')
print(a[:b1], end='')
[print(a[i], end='') for i in range(b2, b1, -1)]
print(a[b2:])

# In the hole in the ground there lived a hobbit