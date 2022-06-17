# Вычислить сумму элементов набора чисел

from random import randint


def func(lst):
    if lst == []:
        return 0
    else:
        summa = func(lst[1:])
        summa = summa + lst[0]
        return summa


lst = []
i = 0
n = int(input("Введите число N: "))
for i in range(n):
    lst.append(randint(1, 10))
summa = func(lst)
print(f'Список: {lst}\nСумма элементов набора чисел: {summa}')
