# вариант 17
# Из исходного текстового файла (experience.txt) выбрать стаж работы.
# Посчитать количество полученных элементов.

import re

with open('experience.txt', 'r', encoding='utf-8') as exp:
    text = exp.read()
    a = re.findall(r'\b[0-9]+.\w+.[0-9]+.\w*', text)      # findall - поиск всех совпадений в шаблоне
    b = re.findall(r'\b3+.\w{4}\b', text)
    a.append(b[0])
    c = ", ".join(map(str, a))     # map - применяет функцию к каждому элементу итерируемого объекта
    print('Стажи работы: ', c)
    print('Количество стажей работы: ', len(a))
