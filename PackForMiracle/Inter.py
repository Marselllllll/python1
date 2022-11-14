from PackForMiracle import *
while True:
    print('\033[4m\033[32mПоле чудес\033[0m')
    main = int(input('1 - Играть\n2 - Рекорды\n3 - Настройки\n4 - Выход\nВыбор: '))
    if main == 1:
        ex2 = 0
        recc = 0
        l = 0
        word = ''
        lvl = 0
        while ex2 != 3 and l != 3:
            ex2 = 0
            if recc != 0:
                rec = recc
            else:
                rec = 0
            while ex2 != 1 and ex2 != 3:
                gr = int(input('Выбор тематики слов:\n1 - Природа\n2 - Техносфера\n3 - Имена\nВыбор: '))
                if gr == 1:
                    word = word_in_file('Nature.txt', 2)
                elif gr == 2:
                    word = word_in_file('Tech.txt', 2)
                else:
                    word = word_in_file('Name.txt', 2)
                if lvl == 0:
                    lvl = int(input('Выбор уровня сложности:\n1 - 7 жизней\n2 - 5 жизней\n3 - 3 жизни\nВыбор: '))
                ex2 = int(input('1 - Играть\n2 - Выбрать заново\n3 - Выход в меню\nВыбор: '))
            if ex2 == 3:
                break
            else:
                m = game(word, lvl)
                if m == 0:
                    rec += 1
                    l = int(input('1 - Продолжить играть\n2 - Выбрать новую тему\n3 - Выход в меню\nВыбор: '))
                    if l == 1:
                        recc = rec
                else:
                    l = int(input('1 - Продолжить играть\n2 - Выбрать новую тему\n3 - Выход в меню\nВыбор: '))
            record(rec, lvl)
    if main == 2:
        print('Ваши рекорды')
        with open('Record.txt', mode="r", encoding='cp1251') as re:
            print(re.read())
    if main == 3:
        aa = 0
        while aa != 3:
            aa = int(input('1 - Увидеть список слов\n2 - Изменить список слов\n3 - Выход в меню\nВыбор: '))
            if aa == 1:
                bb = int(input('Выбор тематики слов:\n1 - Природа\n2 - Техносфера\n3 - Имена\nВыбор: '))
                if bb == 1:
                   print(word_in_file('Nature.txt', 1))
                elif bb == 2:
                    print(word_in_file('Tech.txt', 1))
                else:
                    print(word_in_file('Name.txt', 1))
            if aa == 2:
                bb = int(input('Выбор тематики слов:\n1 - Природа\n2 - Техносфера\n3 - Имена\nВыбор: '))
                if bb == 1:
                    llst = word_in_file(r'Nature.txt', 3)
                    lllst = nka(llst)
                    with open('Nature.txt', encoding='cp1251', mode='w') as text:
                        text.writelines(lllst)
                elif bb == 2:
                    llst = word_in_file(r'Tech.txt', 3)
                    lllst = nka(llst)
                    with open('Tech.txt', encoding='cp1251', mode='w') as text:
                        text.writelines(lllst)
                else:
                    llst = word_in_file(r'Name.txt', 3)
                    lllst = nka(llst)
                    with open('Name.txt', encoding='cp1251', mode='w') as text:
                        text.writelines(lllst)
    if main == 4:
        break