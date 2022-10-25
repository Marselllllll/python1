from random import choice


def monty_hall(iter):
    """

    :param iter: араметр, подающий на вход целое количество итераций для проверки.
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