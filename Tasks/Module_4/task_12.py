from calendar import monthrange
a, b = map(int, input('Введите числовое обозначение месяца и день через пробел: ').split())
c = monthrange(2022, a)
if a == 12 and b == 31:
    print('1-1-2023')
elif b+1 > c[1]:
    print(f'1-{a+1}-2022')
else:
    print(f'{b+1}-{a}-2022')