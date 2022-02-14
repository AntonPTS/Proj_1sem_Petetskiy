# вариант 17
# В последовательности на n целых чисел умножить все элементы на последний минимальный элемент.

import random       # импортирование random
m = 0
a = []
b = random.randint(5, 20)
while m < b:
    k = random.randint(1, 100)
    m += 1
    a.append(k)
print('Начальные значения: ', end='')
print(a)
ind = a.index(min(a))       # index(min()) - получение индекса минимального элемента


def func(c):        # def - функция
    y = 0
    if y <= b:
        yield [c[ind] * c[y] for c[y] in c]     # yield - генератор
        y += 1


n = list(func(a))
print('Новые значения: ', end='')
print(*n)
