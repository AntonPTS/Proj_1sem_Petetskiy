# Вычислить количество отрицательных чисел в наборе

from random import randint


def func(lst):
    if lst == []:
        return 0
    else:
        summa = func(lst[1:])
        if lst[0] < 0:
            summa = summa + 1
        return summa


lst = []
i = 0
n = int(input("Введите число N: "))
for i in range(n):
    lst.append(randint(-6, 2))
summa = func(lst)
print(f'Список: {lst}\nКоличество отрицательных чисел в наборе: {summa}')
