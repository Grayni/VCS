# Sum of numbers
num = input('Введите число: ')


# 1. Simple solution
print(int(num) + int(num * 2) + int(num * 3))


# 2. Complex solution
value = 0
i = 3

while i > 0:
    value += int(num * i)
    i -= 1

print(value)
