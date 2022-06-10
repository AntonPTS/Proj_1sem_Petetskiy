# Перевод из десятичной системы исчисления в двоичную

import math


def func(n, i):
    if n > 0:
        p = n % 2
        return func(n//2, i+1) + int(p*math.pow(10, i))
    else:
        return 0


i = 0
n = int(input("Введите число: "))
result = func(n, i)
print(result)
