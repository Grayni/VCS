# The sum of the two
lst = []

try:
    lst = list(map(int, input('Введите через пробел 3 числа: ').split()))
except ValueError:
    print('Введены недопустимые значения.')
    exit()


def my_func(a, b, c):
    """
    :param a: int
    :param b: int
    :param c: int
    :return: sum ~ max int and middle int
    """

    arr = [a, b, c]
    return sum(arr) - min(arr)


try:
    print(my_func(*lst))
except TypeError:
    if len(lst) < 3:
        print('Введено недостаточно данных.')
    elif len(lst) > 3:
        print('Значений задано больше трех.')

