# Degree
X, Y = float(), int()

try:
    X = float(input('Введите действительное положительное число X: '))
    Y = int(input('Введите целое отрицательное число Y: '))
except ValueError:
    print('Введены неккоректные данные.')
    exit()

if Y >= 0:
    print('Число Y должно быть отрицательным.')
    exit()


def my_func_1(x, y):
    return x**y


def my_func_2(x, y):
    degree = 1

    for i in range(1, abs(y) + 1):
        degree *= 1/x

    return degree


print(f'1 функция: {my_func_1(X, Y)}')
print(f'2 функция: {my_func_2(X, Y)}')





