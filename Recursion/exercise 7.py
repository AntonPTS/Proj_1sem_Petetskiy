# Определение максимального элемента списка

from random import randint


def func(lst):
    if len(lst) > 1:
        maxi = func(lst[1:])
        if lst[0] < maxi:
            return maxi
        else:
            return lst[0]
    if len(lst) == 1:
        return lst[0]


lst = []
n = int(input("Введите число: "))
for i in range(n):
    lst.append(randint(1, 100))
maximum = func(lst)
print(lst)
print(maximum)
