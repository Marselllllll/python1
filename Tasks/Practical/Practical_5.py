def read(name):
    try:
        text = []
        text = open(name, mode='r')
    except:
        print('Ошибка')
    else:
        lst = text.readlines()
        print(lst)
    finally:
        if type(text) == '_io.TextIOWrapper':
            print(type(text))

read(r'C:\Users\Student\PycharmProjects\python3\Tasks\Practical\num')
