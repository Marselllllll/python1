from random import choice
from typing import Any


def Word_in_file(group: str, typ: int) -> Any:
    """
    :param group: Параметр (type: str), подающий на вход абсолютный путь к группе слов.
    :param typ: Параметр (type: int), подающий на вход тип взаимодейтсвия с "Str" (1 - для возвращения строки
    со всеми словами; 2 - для выбора 1 слова.; 3 - для удаления слова).
    :return: Либо слово (type: str), либо список слов (type: list)
    """
    with open(group, mode='a+', encoding='UTF-8') as words:
        words.seek(0)
        if typ == 1:
            wordlist = words.read()
            return wordlist
        else:
            words.seek(0)
            wordlist = Normalize(words.readlines())
            if typ == 2:
                word = choice(wordlist)
                return word
            else:
                a = int(input('1 - Удалить слово\n2 - Добавить слово\nВыбор: '))
                wordlist = Del_add_word(a, wordlist)
                return wordlist


def Del_add_word(v: int, lst: list) -> list:
    """
    :param v: Параметр (type: int), подающий на вход выборочное число (1 или 2).
    :param lst: Параметр (type: list), подающий на вход список слов.
    :return: Список (type: list), в измененном отнсительно выбора виде.
    """
    if v == 1:
        check: int = 0
        while check != 1:
            word: str = input('Введите слово, которое хотите удалить: ').upper()
            if lst.count(word) > 0:
                lst.remove(word)
                check = 1
            else:
                check = int(input('Такого слова нет в файле\n0 - Ввести слово заново, 1 - Выйти\nВыбор: '))
        return lst
    else:
        word = input('Введите слово, которое хотите добавить: ').upper()
        lst.append(word)
        return lst


def Normalize(lst: list) -> list:
    """
    :param lst: Параметр (type: list), подающий на вход список для нормализации.
    :return: Список (type: list), возвращаемый функцией в нормализированном виде.
    """
    norm_lst: list = []
    for i in lst:
        if i.find('\n') == -1:
            norm_lst.append(i)
        else:
            norm_lst.append(i[:-1])
    return norm_lst


def Nka(lst: list) -> list:
    """
    :param lst: Параметр (type: list), подающий на вход список для
     дальнейшего добавления спец.символа "\n" к его элементам.
    :return: Список (type: list), возвращаемый функцией
     с добавленными к каждому элементу параметра спец.символами "\n"/
    """
    lst1: list = []
    for i in lst[:-1]:
        lst1.append(i + '\n')
    lst1.append(lst[len(lst) - 1])
    return lst1
