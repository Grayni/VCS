from random import randint

with open('dir/s5_sum.txt', 'w+', encoding='utf-8') as f:
    x = randint(10, 40)
    lst = []

    for i in range(x):
        lst.append(randint(0, 100))
    else:
        print(*lst, file=f)

    f.seek(0)
    lst_nums = list(map(int, f.read().split()))
    print(sum(lst_nums))
