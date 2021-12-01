# вариант 17
# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенными пробелами
# (одним или несколькими). Вывести строку, содержащую эти же слова, разделенные одним пробелом
# и расположенные в алфавитном порядке.

s = input("Введите предложение заглавными русскими буквами: ")
a = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
     "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", " "]
for i in range(0, len(s)):          # len - возвращает количество элементов в объекте
    if s[i] in a:
        continue
    else:
        print("Вы ввели не то, что требуется!")
        exit(0)         # exit - выход из программы
g = s.split()       # split - разбивает строку на части и возвращает эти части списком
h = " ".join(sorted(g, reverse=False))      # join - преобразование списка в строку,
# sorted - возвращает отсортированный список, reverse - параметр, который сортирует список по убыванию или возрастанию
print(h)