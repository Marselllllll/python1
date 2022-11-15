a = input('Введите строку: ')
b1 = a.index('h')
b2 = a.rindex('h')
print(a[:b1+1], end='')
for i in a[b1+1:b2]:
    if i == 'h':
        print('H', end='')
    else:
        print(i, end='')
print(a[b2:])

# In the hole in the ground there lived a hobbit