# Возведение числа x в степень y


def func(x, y):
    if y == 0:
        return 1
    if y > 0:
        return x * func(x, y-1)
    if y < 0:
        return f'1/{x * func(x, -y-1)}'


x = int(input("Введите число X: "))
y = int(input("Введите число Y: "))
result = func(x, y)
print(result)
