def norm_nomer(nomer):
    nomer = nomer.replace(' ','').replace('-','')
    if nomer[:2] == '+7' and len(nomer) == 12:
        return nomer
    if nomer[0] == '8' and len(nomer) == 11:
        nomer = nomer.replace('8','+7',1)
        return nomer
    if nomer[0] == '9' and len(nomer) == 10:
        nomer = '+7' + nomer
        return nomer
    else:
        return 'Неправильно набран номер'

def norm_name(name):
    name = name.title()
    return name

def check_kniga():
    for i in  kniga:
        print(i, kniga[i])

def delete_name():
    name = input('Введите  имя: ')
    namee = norm_name(name)
    del kniga[namee]

def new_name():
    name = input('Введите ФИО: ')
    nomer = input('Введите номер: ')
    g = norm_nomer(nomer)
    v = norm_name(name)
    kniga[v] = g
def renew_name():
    name = input('Введите старое имя: ')
    namee = norm_name(name)
    new_name = input('Введите новое имя: ')
    new_namee = norm_name(new_name)
    kniga[new_namee] = kniga.pop( namee)
def renew_nomer():
    name = input('Введите имя: ')
    namee = norm_name(name)
    new_nomer = input('Введите новый номер: ')
    new_nomerr = norm_nomer(new_nomer)
    kniga[namee] = new_nomerr

kniga = {}

while True:
    ch = int(input('1 - новый контакт\n2 - изменить имя\n3 - изменить номер\n4 - удалить контакт\n5 - посмотреть книгу\nВвод: '))
    if ch == 1:
        a = new_name()
    if ch == 2:
        a = renew_name()
    if ch == 3:
        a = renew_nomer()
    if ch == 4:
        a =  delete_name()
    if ch == 5:
        a = check_kniga()
