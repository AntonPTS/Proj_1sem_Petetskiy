# вариант 17
# Из исходного текстового файла (experience.txt) выбрать стаж работы.
# Посчитать количество полученных элементов.

import re

p = re.compile(r'[0-9]')
with open('experience.txt', 'r', encoding='utf-8') as exp:
    text = exp.read()
    a = re.findall(r'\d+', text)      # findall - поиск всех совпадений в шаблоне
l1 = []
i = 0
b = len(a)
while i < b:
    l1.append(int(a[i]))
    i += 2
p = " ".join(map(str, l1))      # map - применяет функцию к каждому элементу итерируемого объекта
o = p.split(' ')      # split - возвращает список слов в строке
l2 = []
n = 1
while n < b:
    l2.append(int(a[n]))
    n += 2
p1 = " ".join(map(str, l2))
o1 = p1.split(' ')
s = [x * 12 for x in l1]        # списковое включение
p2 = " ".join(map(str, s))
o2 = p2.split(' ')
s2 = []
for t in range(len(l2)):
    g1 = s[t] + l2[t]
    s2.append(g1)
else:
    s2.append(s[len(s)-1])
p3 = ", ".join(map(str, s2))
o3 = p3.split(', ')
print(f'Стажи работы (в месяцах): {p3}')
k = len(o3)
print(f'Количество стажей работы: {k}')
