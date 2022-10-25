from random import randint
from random import choice

def birthday(iter):
    """

    :param iter: Параметр, подающий на вход целое количество итераций для проверки.
    :return: Число, возвращаемое функцией в виде процента совпадений дат относительного общего кол-ва итераций.
    """
    itog = 0
    for i in range(0, iter):
        count_people = randint(23, 100)
        lst = []
        for n in range(0, count_people):
            month = randint(1, 12)
            day = randint(1, 28)
            date = [day, month]
            lst.append(date)
        for l in lst:
            if lst.count(l) > 1:
                itog += 1
                break
    procent = int(100 * itog / iter)

    return procent

def monty_hall(iter):
    """

    :param iter: Параметр, подающий на вход целое количество итераций для проверки.
    :return:  Число, возвращаемое функцией в виде процента выигрышных игр при изменении выбора относительного общего кол-ва итераций.
    """
    c1 = 0
    c2 = 0
    n1 = 0
    n2 = 0

    for i in range(0, iter):
        a = [0, 0, 1]
        b1 = choice(a)
        a.remove(0)
        b2 = choice(a)
        if b1 == b2:
            if b1 == 1:
                c1 = c1 + 1
            else:
                c2 = c2 + 1
        else:
            if b2 == 1:
                n1 = n1 + 1
            else:
                n2 = n2 + 1
    s2 = n1 // ((n1 + n2) // 100)

    return s2