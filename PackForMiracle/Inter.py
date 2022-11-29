from PackForMiracle import *
import os

while True:
    print('\033[4m\033[32mПоле чудес\033[0m')
    main: int = int(input('1 - Играть\n2 - Рекорды\n3 - Настройки\n4 - Выход\nВыбор: '))
    if main == 1:
        choose1: int = 0
        recc: int = 0
        prodol: int = 0
        word: str = ''
        lvl: int = 0
        while choose1 != 3 and prodol != 3:
            choose1 = 0
            if recc != 0:
                rec: int = recc
            else:
                rec = 0
            while choose1 != 1 and choose1 != 3:
                gr: int = int(input('Выбор тематики слов:\n1 - Природа\n2 - Техносфера\n3 - Имена\nВыбор: '))
                if gr == 1:
                    word: str = Word_in_file(os.path.dirname(__file__) + '\\Nature.txt', 2)
                elif gr == 2:
                    word = Word_in_file(os.path.dirname(__file__) + '\\Tech.txt', 2)
                else:
                    word = Word_in_file(os.path.dirname(__file__) + '\\Name.txt', 2)
                if lvl == 0:
                    lvl = int(input('Выбор уровня сложности:\n1 - 7 жизней\n2 - 5 жизней\n3 - 3 жизни\nВыбор: '))
                choose1 = int(input('1 - Играть\n2 - Выбрать заново\n3 - Выход в меню\nВыбор: '))
            if choose1 == 3:
                break
            else:
                game: int = Game(word, lvl)
                if game == 0:
                    rec += 1
                    prodol = int(input('1 - Продолжить играть\n2 - Выбрать новую тему\n3 - Выход в меню\nВыбор: '))
                    if prodol == 1:
                        recc = rec
                else:
                    print(f'Загаданное слово: {word}')
                    prodol = int(input('1 - Продолжить играть\n2 - Выбрать новую тему\n3 - Выход в меню\nВыбор: '))
            Record(rec, lvl)
    if main == 2:
        print('Ваши рекорды')
        with open(os.path.dirname(__file__) + '\\Record.txt', mode="r", encoding='UTF-8') as re:
            print(re.read())
    if main == 3:
        see: int = 0
        while see != 3:
            see = int(input('1 - Увидеть список слов\n2 - Изменить список слов\n3 - Выход в меню\nВыбор: '))
            if see == 1:
                choose2: int = int(input('Выбор тематики слов:\n1 - Природа\n2 - Техносфера\n3 - Имена\nВыбор: '))
                if choose2 == 1:
                    print(Word_in_file(os.path.dirname(__file__) + '\\Nature.txt', 1))
                elif choose2 == 2:
                    print(Word_in_file(os.path.dirname(__file__) + '\\Tech.txt', 1))
                else:
                    print(Word_in_file(os.path.dirname(__file__) + '\\Name.txt', 1))
            if see == 2:
                choose2 = int(input('Выбор тематики слов:\n1 - Природа\n2 - Техносфера\n3 - Имена\nВыбор: '))
                if choose2 == 1:
                    lst1: list = Word_in_file(os.path.dirname(__file__) + '\\Nature.txt', 3)
                    lst2: list = Nka(lst1)
                    with open(os.path.dirname(__file__) + '\\Nature.txt', mode='w', encoding='UTF-8') as text:
                        text.writelines(lst2)
                elif choose2 == 2:
                    lst1 = Word_in_file(os.path.dirname(__file__) + '\\Tech.txt', 3)
                    lst2 = Nka(lst1)
                    with open(os.path.dirname(__file__) + '\\Tech.txt', mode='w', encoding='UTF-8') as text:
                        text.writelines(lst2)
                else:
                    lst1 = Word_in_file(os.path.dirname(__file__) + '\\Name.txt', 3)
                    lst2 = Nka(lst1)
                    with open(os.path.dirname(__file__) + '\\Name.txt', mode='w', encoding='UTF-8') as text:
                        text.writelines(lst2)
    if main == 4:
        break
