from calendar import monthrange, month_name
a = int(input('Введите числовое обозначение месяца: '))
b = monthrange(2022, a)
print(f'Дней в {month_name[a]}: {b[1]}')