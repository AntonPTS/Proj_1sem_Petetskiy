# Возврат ряда Фибоначчи


def func(p, a):
    i = len(a)
    if i < 2:
        return []
    n = a[i - 2]
    m = a[i - 1]
    if (n + m) < p:
        a = a + [n + m]
        return func(p, a)
    else:
        return a


p = int(input("Введите число: "))
a = func(p, [0, 1])
print(f'Ряд Фибоначчи: {a}')
