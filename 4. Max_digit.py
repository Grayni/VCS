# Max digit

number = int(input('Введите число: '))
buffer = 0

while number > 0:
    if buffer < number % 10:
        buffer = number % 10

    number //= 10

input(buffer)
