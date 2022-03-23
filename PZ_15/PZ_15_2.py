# вариант 17
# В матрице найти сумму элементов первых двух строк.

import random
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
mat = []
for i in range(n):
    mat.append([random.randint(1, 10) for j in range(m)])       # списковое включение
summa = 0
print(mat)
for i in [0, 1]:
    for j in range(m):
        summa += mat[i][j]
print('Сумма элементов первых двух строк: ', summa)
