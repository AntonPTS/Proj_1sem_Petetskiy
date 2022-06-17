# Вычисление суммы чисел с поддержкой вложенных списков


def func(lst):
    summa = 0
    for i in lst:
        if not isinstance(i, list):
            summa = summa + i
        else:
            summa = summa + func(i)
    return summa


lst = [5, 9, 4, 9, [2, 4, 1, [8, 2]], [3, 5], 7]
summa = func(lst)
print(f'Список: {lst}\nСумма элементов набора чисел: {summa}')
