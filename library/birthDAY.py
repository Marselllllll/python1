from random import randint

def birthday(iter, count_people = 23):
    """

    :param iter: Параметр, подающий на вход целое количество итераций для проверки.
    :param count_people: Параметр, подающий на вход целое количество людей в группе.
    :return: Число, возвращаемое функцией в виде процента совпадений дат относительного общего кол-ва итераций.
    """
    itog = 0
    for i in range(0, iter):
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
    procent = (100 * itog / iter)

    return procent