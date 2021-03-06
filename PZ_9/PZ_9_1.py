# вариант 17
# Даны имена девочек. Определить, какие из этих имен встречаются в группах на всех вторых курсах,
# какие есть только в некоторых группах и какие не встречаются ни в одной из групп.

a = {"Дарья", "Любовь", "Елизавета", "Екатерина", "Александра", "Валентина", "Ольга", "Надежда"}
g1 = {"Марина", "Елизавета", "Любовь"}
g2 = {"Любовь", "Ирина", "Людмила"}
g3 = {"Александра", "Марина", "Любовь", "Ольга"}
p = set(a & g1 & g2 & g3)
print("Имена, которые есть во всех группах: ", p)
k = set()          # set обозначет, что k - множество
if a & g1:          # & обозначает пересечение множеств
    x = a & g1
    k.update(x)         # добавление в множество k одного или нескольких элементов
if a & g2:
    y = a & g2
    k.update(y)
if a & g3:
    z = a & g3
    k.update(z)
print("Имена, которые есть только в некоторых группах: ", k - p)
h = a - g1 - g2 - g3
print("Имена, которые не встречаются ни в одной из групп: ", h)
