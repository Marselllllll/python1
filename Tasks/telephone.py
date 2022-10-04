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

def check_kniga(kniga):
    for i in  kniga:
        print(i,kniga[i])
        return kniga

def delete_name(name):
    del kniga[name]

def renew











