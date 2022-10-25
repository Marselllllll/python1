from random import randint

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

