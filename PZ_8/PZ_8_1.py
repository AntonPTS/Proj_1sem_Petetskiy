# вариант 17
# Дан словарь на 6 персон, найти и вывести их средний возраст. (Пример, {"Андрей":32, "Виктор":29, ...}, среднее 26,33)

import random
d = {"Артём": 0, "Владимир": 0, "Никита": 0, "Андрей": 0, "Виктор": 0, "Максим": 0}
a = 0
for c in d:
    k = random.randint(3, 110)
    d[c] = k
    a += d[c]
b = a / 6
print(d)
print(round(b, 1))
