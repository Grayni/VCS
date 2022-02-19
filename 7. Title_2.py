# Title_2
string = input('Введите строку: ')


################################
# If use function in cycle
# For example


def funcs_upper(w):
    return w[0].upper() + w[1:]


lst = string.split()
arr1 = []

# Method upper()
for word in lst:
    arr1.append(funcs_upper(word))

print(f'Method upper:\n{" ".join(arr1)}\n')


##############################


###############################
# Ready functions
# 1 variant
def title_func1(s):
    return s.title()


print(f'Вариант 1.\n{title_func1(string)}\n')


# 2 variant
def title_func2(s):
    lst = s.split()
    arr = []

    for word in lst:
        arr.append(word[0].upper() + word[1:])

    return ' '.join(arr)


print(f'Вариант 2.\n{title_func2(string)}\n')


# 3 variant
def title_func3(s):
    lst = s.split()
    arr = []

    for word in lst:
        arr.append(word.replace(word[0], word[0].upper(), 1))

    return ' '.join(arr)


print(f'Вариант 3.\n{title_func2(string)}')

