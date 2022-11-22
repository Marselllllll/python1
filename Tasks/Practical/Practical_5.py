from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from typing import TextIO

from library import alfavit

# Выбор файла из окна
Tk().withdraw()
filename = askopenfilename()

# Кортеж пути
os.path.splitext(filename)

# Строка пути
extension_tuple: tuple = os.path.splitext(filename)
extension_string: str = ''.join(extension_tuple)

# Проверка расширения
if extension_string.lower().endswith('.txt'):
    # Считывание файла
    try:
        text: TextIO = open(extension_string, mode='r')
        check_count_lines: list = text.readlines()
        line2: str = check_count_lines[1]
    except IndexError:
        print('\033[31m\033[1mОшибка форматирования.\033[0m\nВ файле менее \033[31m\033[1m2-х строк.\033[0m')
    else:
        text.seek(0)
        all_line_list: list = text.readlines()
        line: int = 0
        finish_list: list = []
        check_end: int = 0
        for i in all_line_list:
            line += 1
            value_line: str = i.replace('\n', '')
            value_line = value_line.strip()
            try:
                value_line_check: int = int(value_line)
            except ValueError:
                value_line_list: list = list(value_line)
                check_end = 1
                for j in value_line_list:
                    j: str = j.lower()
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
        finish_count: int = finish_list.pop(0)
        if check_end == 0:
            if finish_count != len(finish_list):
                print('\033[31m\033[1mОшибка форматирования.\033[0m\n'
                      'В строке под номером 1 указано \033[31m\033[1mНеверное количество элементов.\033[0m')
            else:
                print(finish_list)
    finally:
        text.close()
