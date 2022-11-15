def read_file(name):
    text = open(name, mode='r')
    stroka1 = text.read()
    text.close()
    stroka = stroka1.replace('\n', ' ')
    i = 0
    s = ''
    while i != len(stroka):
        if ord(stroka[i]) >= 1040 and ord(stroka[i]) <= 1103 or ord(stroka[i]) == 1025 or ord(stroka[i]) == 1105:
            s += stroka[i].lower()
        elif stroka[i] == ' ' or stroka[i] == '-' or stroka[i] == '_':
            if stroka[i+1] != ' ':
                s += stroka[i]
        i += 1
    lst = s.split(sep=' ')
    i = 0
    lst1 = []
    while i != len(lst):
        if lst1.count(lst[i] + '\n') == 0:
            lst1.append(lst[i] + '\n')
        i += 1
    lst1.sort()
    m = lst1[len(lst1)-1]
    lst1.pop(len(lst1)-1)
    n = m.replace('\n', '')
    lst1.append(n)
    return lst1


def save_file(name, lst):
    with open(name, mode='w', encoding='Windows-1251') as text:
        a = [f'Количество уникальных слов: {len(lst)}\n', '========================\n']
        text.writelines(a)
        text.writelines(lst)


a = read_file('data.txt')
b = input('Придумайте имя файля для сохранения уникальных слов из файла data.txt: ')
save_file(b, a)
