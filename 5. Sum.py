# Sum
lst = input('Стоп-слово: stop. Введите значения через пробел: ').split()  # can be used map with int


def sum_func(arr):
    buffer = 0
    while True:
        if buffer != 0:
            arr = input('Введите еще ряд чисел:  ').split()

        for num in arr:
            if num == 'stop':
                print(f'Конечный результат: {buffer}')
                return
            else:
                buffer += int(num)

        print(buffer)


sum_func(lst)
