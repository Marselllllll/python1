a = input('Введите трехзначное число: ')
b = list(a)
c = b.copy()
c.sort()
if b == c:
    print('Да')
else:
    print('Нет')