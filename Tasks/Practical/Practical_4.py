from typing import TextIO


def read_file(name: str) -> list:
    """
    :param name: Параметр (type: str), подающий на вход путь к файлу для последующего чтения.
    :return: Значение (type: list), возвращаемое функцией в виде списка всех слов из прочитанного файла.
    """
    text: TextIO = open(name, mode='r')
    stroka0: str = text.read()
    text.close()
    stroka1: str = stroka0.replace('\n', ' ')
    i: int = 0
    strokaend: str = ''
    while i != len(stroka1):
        if 1040 <= ord(stroka1[i]) <= 1103 or ord(stroka1[i]) == 1025 or ord(stroka1[i]) == 1105:
            strokaend += stroka1[i].lower()
        elif stroka1[i] == ' ' or stroka1[i] == '-' or stroka1[i] == '_':
            if stroka1[i+1] != ' ':
                strokaend += stroka1[i]
        i += 1
    lst0: list = strokaend.split(sep=' ')
    i = 0
    lstend: list = []
    while i != len(lst0):
        if lstend.count(lst0[i] + '\n') == 0:
            lstend.append(lst0[i] + '\n')
        i += 1
    lstend.sort()
    end_str0: str = lstend[len(lstend)-1]
    lstend.pop(len(lstend)-1)
    end_strend: str = end_str0.replace('\n', '')
    lstend.append(end_strend)
    return lstend


def save_file(name: str, lst: list) -> None:
    with open(name, mode='w', encoding='Windows-1251') as text:
        beginning: list = [f'Количество уникальных слов: {len(lst)}\n', '================================']
        text.writelines(beginning)
        text.writelines(lst)


file: list = read_file('data.txt')
name: str = input('Придумайте имя файля для сохранения уникальных слов из файла data.txt: ')
save_file(name, file)
