from random import choice
def word_in_file(group, typ):
    with open(group, encoding='cp1251', mode='a+') as words:
        words.seek(0)
        if typ == 1:
            wordlist = words.read()
            return wordlist
        else:
            words.seek(0)
            wordlist = normalize(words.readlines())
            if typ == 2:
                word = choice(wordlist)
                return word
            else:
                a = int(input('1 - Удалить слово\n2 - Добавить слово\nВыбор: '))
                wordlist = del_add_word(a, wordlist)
                return wordlist

def del_add_word(v, lst):
    if v == 1:
        m = 0
        while m != 1:
            a = input('Введите слово, которое хотите удалить: ').upper()
            if lst.count(a) > 0:
                lst.remove(a)
                m = 1
            else:
                m = int(input('Такого слова нет в файле\n0 - Ввести слово заново, 1 - Выйти\nВыбор: '))
        return lst
    else:
        a = input('Введите слово, которое хотите добавить: ').upper()
        lst.append(a)
        return lst

def normalize(lst):
    norm_lst = []
    for i in lst:
        if i.find('\n') == -1:
            norm_lst.append(i)
        else:
            norm_lst.append(i[:-1])
    return norm_lst

def nka(lst):
    lst1 = []
    for i in lst[:-1]:
        lst1.append(i + '\n')
    lst1.append(lst[len(lst) - 1])
    return lst1