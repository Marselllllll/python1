import re
import ssl
import urllib.request


def check(string):
    pattern = r'(?<=class="org-widget-header__title-link">).+(?=<)'
    name = re.search(pattern, string)
    try:
        name = name[0]
        return 1
    except:
        return 0

def choosing(pattern, string):
    a1 = re.search(pattern, string)
    try:
        a = a1[0]
        return a
    except:
        pass


ssl._create_default_https_context = ssl._create_unverified_context

string = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()

big_list = []

while check(string) == 1:

    pattern = r'(?<=class="org-widget-header__title-link">).+(?=<)'
    start1 = re.search(pattern, string)
    start = start1.start()

    pattern = r'(?<=\s{4}<\/div>\n\s{2}<\/div>\n<\/div)>'
    end1 = re.search(pattern, string)
    end = end1.end()

    new_string = string[start-40:end]
    string = string[end:]

    pattern = r'(?<=class="org-widget-header__title-link">).+(?=<)'
    name = choosing(pattern, new_string)

    pattern = r'(?<=<span class="org-widget-header__meta org-widget-header__meta--location">\n\s{12}).+'
    adress = choosing(pattern, new_string)
    if adress == None:
        adress = 'Адрес не указан'

    pattern = r'(?<=Телефон<\/span><\/dt>\n\s{12}<dd class="spec__value">).+(?=<)'
    tel_num = choosing(pattern, new_string)
    if tel_num == None:
        tel_num = 'Номер не указан'


    pattern = r'(?<=<dt class="spec__index"><span class="spec__index-inner">Часы работы<\/span><\/dt>' \
          r'\n\s{12}<dd class="spec__value">).+(?=<)'
    work_hour = choosing(pattern, new_string)
    if work_hour == None:
        work_hour = 'Часы работы не указаны'


    pattern = r'(?<=<div class="org-widget-feedback__comment">\n\s{14}<p>\n\s{16}).+'
    feedback = choosing(pattern, new_string)
    if feedback == None:
        feedback = 'Отзыв не написан'


    big_list.append([name, adress, tel_num, work_hour, feedback])

print(big_list)

