a = input('Введите строку: ')
print(a[2])
print(a[-1])
print(a[:5])
print(a[:-2])
[print(a[i], end='') for i in range(0, len(a), 2)]
print(end='\n')
[print(a[i], end='') for i in range(1, len(a), 2)]
print(end='\n')
[print(a[i], end='') for i in range(len(a)-1, -1, -1)]
print(end='\n')
[print(a[i], end='') for i in range(len(a)-1, -1, -2)]
print(end='\n')