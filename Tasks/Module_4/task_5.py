a, b =  map(int, input("Введите Ваши числа через пробел: ").split())
if a < 0:
    if b < 0:
        print("Нет")
    else:
        print("Да")
else:
    print("Да")