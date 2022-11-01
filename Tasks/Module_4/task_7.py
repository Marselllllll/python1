a = input('Введите четырехзначное число: ')
b = list(a)
c = b.copy()
b.reverse()
if b == c:
    print('Да')
else:
    print('Нет')