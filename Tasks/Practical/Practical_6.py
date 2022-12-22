import re
#[время]: Поезд № (номер) из/в город


def find(string: str):
    name = re.findall(r'(?<=Рейс ).*', string)
    for i in name:
        all_info = i.split(" ")
        print(f'[{all_info[5]}]: Поезд №{all_info[0]} {all_info[2]} {all_info[3]}')


with open("journal.txt", encoding="UTF8") as text:
    wordlist = text.read()
    find(wordlist)
