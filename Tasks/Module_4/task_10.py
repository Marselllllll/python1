a, b = map(int, input('Введите координаты клетки шахматной доски 8х8 через пробел: ').split())
if a % 2 == 0:
    if b % 2 == 0:
        print('Черная')
    else:
        print('Белая')
else:
    if b % 2 == 0:
        print('Белая')
    else:
        print('Черная')