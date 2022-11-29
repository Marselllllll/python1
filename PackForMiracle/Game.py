import os


def Game(word: str, lvl: int) -> int:
    """
    :param word: Параметр (type: str), подающий на вход слово для игры.
    :param lvl: Параметр (type: int), подающий на вход выбранный уровень для игры.
    :return: Значение (type: int), возвращаемое функцией для дайнейшего применения в выборе (1 или 2).
    """
    if lvl == 1:
        lvl = 7
    elif lvl == 2:
        lvl = 5
    else:
        lvl = 3
    lst: list = list(word)
    secret: list = ['\u25A0']*len(lst)
    while lvl != 0 and secret != lst:
        for i in secret:
            print(i, end=' ')
        print(f'❤x{lvl}')
        vvod: str = input("Введите букву или слово целиком: ").upper()
        if vvod == word:
            secret = lst
        elif lst.count(vvod) > 0:
            secret.pop(lst.index(vvod))
            secret.insert(lst.index(vvod), vvod)
        else:
            print('\033[31m Неправильно\033[0m, прощайся с жизнью, котик.')
            lvl -= 1
    if secret == lst:
        print('Выиграл!')
        return 0
    else:
        print('Проиграл!')
        return 1

def Record(rec: int, lvl: int) -> None:
    """
    :param rec: Параметр (type: int), подающий на вход рекорд.
    :param lvl: Параметр (type: int), подающий на вход уровень рекорда.
    :return: None
    """
    with open(os.path.dirname(__file__) + '\\Record.txt', mode="w+", encoding='UTF-8') as text:
        zapis: str = f"Рекорд: {rec}; Сложность: {lvl} "
        text.write(zapis)
