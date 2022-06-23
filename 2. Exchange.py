# Exchange numbers in List
lst = []

while True:
    lst.append(input('Enter something: '))

    if len(lst) % 2 == 0:
        lst[-1], lst[-2] = lst[-2], lst[-1]

    print(lst)
