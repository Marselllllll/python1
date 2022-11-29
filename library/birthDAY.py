from random import randint


def birthday(iter: int, count_people: int = 23) -> float:
    """
    :param iter: Параметр, подающий на вход целое количество итераций для проверки.
    :param count_people: Параметр, подающий на вход целое количество людей в группе.
    :return: Число, возвращаемое функцией в виде процента совпадений дат относительного общего кол-ва итераций.
    """
    itog: int = 0
    for i in range(0, iter):
        lst: list = []
        for n in range(0, count_people):
            month: int = randint(1, 12)
            day: int = randint(1, 28)
            date: list = [day, month]
            lst.append(date)
        for l in lst:
            if lst.count(l) > 1:
                itog += 1
                break
    procent: float = (100 * itog / iter)

    return procent
