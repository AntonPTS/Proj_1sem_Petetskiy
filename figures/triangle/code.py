__all__ = ['triangle_perimeter', 'triangle_area']
from math import sqrt
a = 7
b = 2
c = 8


def triangle_perimeter():
    a1 = int(input('Введите длину стороны a или значение <=0: '))
    b1 = int(input('Введите длину стороны b или значение <=0: '))
    c1 = int(input('Введите длину стороны c или значение <=0: '))
    if a1 + b1 + c1 > 0:
        return print('Периметр треугольника: ', a1 + b1 + c1)
    else:
        return print('Периметр треугольника: ', a + b + c)


def triangle_area():
    a1 = int(input('Введите длину стороны a или значение <=0: '))
    b1 = int(input('Введите длину стороны b или значение <=0: '))
    c1 = int(input('Введите длину стороны c или значение <=0: '))
    if a1 + b1 + c1 > 0:
        p = (a1 + b1 + c1) / 2
        return print('Площадь треугольника: ', sqrt(p*(p-a1)*(p-b1)*(p-c1)))
    else:
        p = (a + b + c) / 2
        return print('Площадь треугольника: ', sqrt(p*(p-a)*(p-b)*(p-c)))
