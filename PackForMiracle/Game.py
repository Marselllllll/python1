def game(word, lvl):
    if lvl == 1:
        lvl = 7
    elif lvl == 2:
        lvl = 5
    else:
        lvl = 3
    a = list(word)
    c = ['\u25A0']*len(a)
    while lvl != 0 and c != a:
        for i in c:
            print(i, end=' ')
        print(f'❤x{lvl}')
        m = input("Введите букву или слово целиком: ").upper()
        if m == word:
            c = a
        elif a.count(m) > 0:
            c.pop(a.index(m))
            c.insert(a.index(m), m)
        else:
            print('\033[31m Неправильно\033[0m, прощайся с жизнью, котик.')
            lvl -= 1
    if c == a:
        print('Выиграл!')
        return 0
    else:
        print('Проиграл!')
        return 1

def record(rec, lvl):
    with open(r'C:\Users\Student\PycharmProjects\python3\PackForMiracle\Record.txt', encoding='cp1251', mode="w+") as text:
        zn = f"Рекорд: {rec}; Сложность: {lvl} "
        text.write(zn)

