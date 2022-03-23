__all__ = ['circle_perimeter', 'circle_area']
default_radius = 5


def circle_perimeter():
    radius = int(input('Введите радиус или 0: '))
    if radius > 0:
        return print('Длина окружности: ', radius * 2 * 3.14)
    else:
        return print('Длина окружности: ', default_radius * 2 * 3.14)


def circle_area():
    radius = int(input('Введите радиус или 0: '))
    if radius > 0:
        return print('Площадь окружности: ', radius ** 2 * 3.14)
    else:
        return print('Площадь окружности: ', default_radius ** 2 * 3.14)
