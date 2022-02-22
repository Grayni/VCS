from itertools import cycle, count


x = int(input('Введите начальное число: '))
min_X = x * 5
max_X = x * 10
y = int(input(f'Введите конечное число от {min_X} до {max_X}: '))
arr = []  # list out func 1 for func 2


# 1 func
def func_counter(initial, iteration):
    lst = []
    for counter in count(initial):
        lst.append(counter)
        if counter == iteration:
            print(lst)
            return lst


# Check value y
if min_X <= y <= max_X:
    arr = func_counter(x, y)
else:
    print('Не верное число итераций. Попробуйте позже.')
    exit()


repeat = int(input('\nвведите количество итераций: '))


# func 2
def func_cycle(lst, i):
    for num in cycle(lst):
        i -= 1
        print(num)
        if i == 0:
            break


func_cycle(arr, repeat)

