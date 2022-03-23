__all__ = ['square_perimeter', 'square_area']
a = 15


def square_perimeter():
    b = int(input('Введите длину стороны или 0: '))
    if b > 0:
        return print('Периметр квадрата: ', 4 * b)
    else:
        return print('Периметр квадрата: ', 4 * a)


def square_area():
    b = int(input('Введите длину стороны или 0: '))
    if b > 0:
        return print('Площадь квадрата: ', b ** 2)
    else:
        return print('Площадь квадрата: ', a ** 2)
