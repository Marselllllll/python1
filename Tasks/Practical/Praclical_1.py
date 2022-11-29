from random import choice


def monty_hall(iter: int) -> int:
    """
    :param iter: Параметр, подающий на вход целое количество итераций для проверки.
    :return:  Число, возвращаемое функцией в виде процента выигрышных игр при изменении выбора
     относительного общего кол-ва итераций.
    """
    c1: int = 0
    c2: int = 0
    n1: int = 0
    n2: int = 0

    for i in range(0, iter):
        lst: list = [0, 0, 1]
        random_choose1: int = choice(lst)
        lst.remove(0)
        random_choose2: int = choice(lst)
        if random_choose1 == random_choose2:
            if random_choose1 == 1:
                c1 = c1 + 1
            else:
                c2 = c2 + 1
                # Значения c1 и c2 нужны для того, чтобы при неоходимости посчитать кол-во побед и поражений в случае
                # отсутсвия изменения выбора.
        else:
            if random_choose2 == 1:
                n1 = n1 + 1
            else:
                n2 = n2 + 1
    s2: int = n1 // ((n1 + n2) // 100)

    return s2


print(monty_hall(100000))
