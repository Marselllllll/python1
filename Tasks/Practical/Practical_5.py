from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from library import alfavit

# Выбор файла из окна
Tk().withdraw()
filename = askopenfilename()

# Кортеж пути
os.path.splitext(filename)

# Строка пути
extension_tuple = os.path.splitext(filename)
extension_list = ''.join(extension_tuple)

text = []
# Проверка расширения
if extension_list.lower().endswith('.txt'):
    # Считывание файла
    try:
        text = open(extension_list, mode='r')
        check_count_lines = text.readlines()
        line2 = check_count_lines[1]
    except IndexError:
        print('\033[31m\033[1mОшибка форматирования.\033[0m\nВ файле менее \033[31m\033[1m2-х строк.\033[0m')
    else:
        text.seek(0)
        all_line_list = text.readlines()
        line = 0
        finish_list = []
        check_end = 0
        for i in all_line_list:
            line += 1
            value_line = i.replace('\n', '')
            value_line = value_line.strip()
            try:
                value_line_check = int(value_line)
            except ValueError:
                value_line_list = list(value_line)
                check_end = 1
                for j in value_line_list:
                    j = j.lower()
                    if j == ' ':
                        print(f'\033[31m\033[1mОшибка форматирования.\033[0m\n'
                              f'В строке под номером {line} есть символ \033[31m\033[1m"Пробел".\033[0m')
                        break
                    elif alfavit.russian.count(j) != 0:
                        print(f'\033[31m\033[1mОшибка форматирования.\033[0m\n'
                              f'В строке под номером {line} есть символ \033[31m\033[1mРусского алфавита.\033[0m')
                        break
                    elif alfavit.english.count(j) != 0:
                        print(f'\033[31m\033[1mОшибка форматирования.\033[0m\n'
                              f'В строке под номером {line} есть символ \033[31m\033[1mАнглийского алфавита.\033[0m')
                        break
                    else:
                        print(f'\033[31m\033[1mОшибка форматирования.\033[0m\n'
                              f'В строке под номером {line} есть \033[31m\033[1mНебуквенный символ.\033[0m')
                        break

            else:
                finish_list.append(value_line_check)
        finish_count = finish_list.pop(0)
        if check_end == 0:
            if finish_count != len(finish_list):
                print('\033[31m\033[1mОшибка форматирования.\033[0m\n'
                      'В строке под номером 1 указано \033[31m\033[1mНеверное количество элементов.\033[0m')
            else:
                print(finish_list)
    finally:
        text.close()
