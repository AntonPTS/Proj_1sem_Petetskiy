# вариант 17
# Дан список размера N. Найти номер двух ближайших элементов из этого спика
# (то есть элементов с наименьшим модулем разности)
# и вывести эти номера в порядке возрастания.

try:        # обработка исключений
    import random       # импортирование модуля random
    n = int(input("Введите размер списка: "))
    a = []
    b = 0
    while b < n:
        if n > 0:
            k = random.randint(1, 100)
            b += 1
            a.append(k)
        else:
            break           # выход из цикла
    if n > 0:
        print(a)
    d = 0
    e = 1
    z = []
    while e < n:
        x = a[d]
        y = a[e]
        if x > y:
            h = x - y
        else:
            h = y - x
        d += 1
        e += 1
        z.append(h)
    index = z.index(min(z))         # index позволяет узнать индекс элемента в списке
    print("Номер первого числа:", index)
    print("Номер второго числа:", index+1)
except ValueError:
    print("Вы ввели не то, что требуется!")
