# вариант 17
# Даны a, b, c вещественного типа.
# Если значения упорядочены по возрастанию, то удвоить,
# в противном случае заменить на противоположное.

try:            # обработка исключений
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    if a < b < c:           # проверяет, упорядочены ли значения a, b, c по возрастанию
        print(f"Значения чисел упорядочены по возрастанию {a * 2, b * 2, c * 2}")
    else:
        print(f"Значения чисел не упорядочены по возрастанию {a * -1, b * -1, c * -1}")
except ValueError:
    print("Что-то пошло не так, попробуйте снова!")
