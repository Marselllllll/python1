a, b = map(int, input('Введите координаты 1 клетки шахматной доски 8х8 через пробел: ').split())
a1, b1 = map(int, input('Введите координаты 2 клетки шахматной доски 8х8 через пробел: ').split())
def f(m,n):
    if m % 2 == 0:
        if n % 2 == 0:
            c='Черная'
        else:
            c='Белая'
    else:
        if n % 2 == 0:
            c='Белая'
        else:
            c='Черная'
    return c
if f(a, b) == f(a1, b1):
    print('Да')
else:
    print('Нет')
