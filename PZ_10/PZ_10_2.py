# вариант 17
# Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое, количество знаков препинания.
# Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно поставив последнюю строку между первой и второй.

f = open("text18-17.txt", "r", encoding='utf-8')    # open создает/открывает .txt файл
print("Содержимое файла: ")
s = f.read()        # read читает содержимое всего файла
print(s)
print()
f.close()

f = open("text18-17.txt", "r", encoding='utf-8')
i = 1
y = str()       # str дает понять, что y - это строка
b = [",", ":", ".", "—", "!"]
while i < 8:
    t = f.readline()      # readline читает одну строку
    y += t
    i += 1
j = 0
for u in range(0, len(y)):
    if y[u] in b:
        j += 1
print("Количество знаков препинания: ", j)
f.close()

f1 = open("file102.txt", "w", encoding='utf-8')
f = open("text18-17.txt", "r", encoding='utf-8')
h = f.readlines()      # readlines читает все строки и выводит их в виде списка
f1.write(h[0])
x = len(h)
f1.write(h[x - 1] + "\n")
v = 1
while v < 6:
    f1.write(h[v])       # write используется для записи текста в файл
    v += 1
print()
print("file102.txt успешно создан!")
f.close()       # close закрывает файл
f1.close()
