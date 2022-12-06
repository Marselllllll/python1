import re
import ssl
import urllib.request

def check(string):
    pattern = r'(?<=class="org-widget-header__title-link">).+(?=<)'
    name = re.search(pattern, string)
    if name[0] != '':
        return 1
    else:
        return 0

ssl._create_default_https_context = ssl._create_unverified_context

string = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()

big_list = []

while check(string) == 1:

    pattern = r'(?<=class="org-widget-header__title-link">).+(?=<)'
    start1 = re.search(pattern, string)
    start = string.index(start1[0])

    pattern = r'(?<=\s{4}<\/div>\n\s{2}<\/div>\n<\/div>)'
    end1 = re.search(pattern, string)
    end = string.index(end1[0])

    new_string = string[start-40:end]

    pattern = r'(?<=class="org-widget-header__title-link">).+(?=<)'
    name = re.search(pattern, new_string)

    pattern = r'(?<=<span class="org-widget-header__meta org-widget-header__meta--location">\n\s{12}).+'
    adress = re.search(pattern, new_string)

    pattern = r'(?<=Телефон<\/span><\/dt>\n\s{12}<dd class="spec__value">).+(?=<)'
    tel_num = re.search(pattern, new_string)

    pattern = r'(?<=<dt class="spec__index"><span class="spec__index-inner">Часы работы<\/span><\/dt>' \
          r'\n\s{12}<dd class="spec__value">).+(?=<)'
    work_hour = re.search(pattern, new_string)

    pattern = r'(?<=<div class="org-widget-feedback__comment">\n\s{14}<p>\n\s{16}).+'
    feedback = re.search(pattern, new_string)

    big_list.append([name, adress, tel_num, work_hour, feedback])

print(big_list)

