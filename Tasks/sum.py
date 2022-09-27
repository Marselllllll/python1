print('"Генератор примеров" \nВам нужно написать правильный ответ. На каждую итерацию у Вас 3 жизни.')
tr=3
f=-1
while tr !=0:
    f=f+1
    tr=3
    import random
    a1 = random.randint(0, 100)
    a2 = random.randint(0, 100)
    a3 = a1 + a2
    b1=int(input(f'{a1} + {a2} = '))
    if b1 != a3:
        tr = tr-1
        print(f"Неправильно.\nОсталось жизней: {tr}")
        b2 = int(input(f'{a1} + {a2} = '))
        if b2 != a3:
            tr = tr - 1
            print(f"Неправильно.\nОсталось жизней: {tr}")
            b3 = int(input(f'{a1} + {a2} = '))
            if b3 != a3:
                tr = tr - 1
                print(f"Неправильно.\nВы проиграли.\nВсего правильных ответов: {f}")


