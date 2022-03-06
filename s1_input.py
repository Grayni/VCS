from itertools import count

print('Введите несколько строк\nПустая строка - Exit')
f = open('dir/s1_input.txt', 'w+', encoding='utf-8')

for i in count(1):
    string = input(f'{i}: ')

    if not string:
        print('Ввод завершен.\n\nПросмотр файла:\n______________\n')
        f.seek(0)
        print(f.read())
        f.close()
        break

    print(string, file=f)
