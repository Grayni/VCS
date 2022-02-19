# Division
dividend = int(input('Введите делимое: '))
divider = int(input('Введите делитель: '))


def divide(x, y):
    """
    # Number division function
    :param x: dividend
    :param y: divider
    :return: int or float value
    """

    try:
        z = x / y
    except ZeroDivisionError:
        divider_2 = int(input('\nНа 0 делить нельзя.\nВведите делитель отличный от 0: '))
        divide(dividend, divider_2)
        return

    result = z if z % 1 else int(z)
    print(f'\nРезультат деления: {result}')


divide(dividend, divider)


"""
# An alternative way to handle the division by 0 error
def divide_2(x, y):
    if y == 0:
        divider_2 = int(input('\nНа 0 делить нельзя.\nВведите делитель отличный от 0: '))
        divide(dividend, divider_2)
        return

    z = x / y

    result = z if z % 1 else int(z)
    print(f'\nРезультат деления: {result}')


divide_2(dividend, divider)
"""