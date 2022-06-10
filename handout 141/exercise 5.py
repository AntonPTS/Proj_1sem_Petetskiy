# Реверсирование числа
import math


def func(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    i = 0
    num = n
    while num > 0:
        i = i + 1
        num = num // 10

    t = n % 10
    res = t * int(math.pow(10, i - 1))
    return res + func(n // 10)


n = int(input("Введите число: "))
number = func(n)
print(number)
