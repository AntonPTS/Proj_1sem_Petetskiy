# вариант 17
# Сгенерировать матрицу на произвольное количество элементов, в которой задается
# преобразование от предыдущего элемента к следующему на произвольное значение.

import random
import math

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
pr = n * m


def matrix(per):      # функция
    e = math.ceil(len(per) / n)       # ceil - округление до ближайшего большего числа

    for x in range(0, len(mat), e):
        func = mat[x: e + x]
        yield func         # yield - генератор


lst = []
[lst.append(random.randint(-3, 3)) for i in range(0, pr-1)]     # списковое включение
mat = [random.randint(-3, 3)]
for i in range(0, pr-1):
    mat.append(mat[i] + lst[i])
print(list(matrix(mat)))
