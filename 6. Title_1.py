# Title_1
word = input('Введите слово: ')


# 1 variant
def title_func1(w):
    return w.title()


print(f'Вариант 1.\n{title_func1(word)}\n')


# 2 variant
def title_func2(w):
    return w[0].upper() + w[1:]


print(f'Вариант 2.\n{title_func2(word)}\n')


# 3 variant
def title_func3(w):
    return w.replace(w[0], w[0].upper(), 1)


print(f'Вариант 3.\n{title_func3(word)}')

