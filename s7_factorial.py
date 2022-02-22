def fact(num):
    initial = 1

    for i in range(1, num + 1):
        initial *= i
        yield initial


for x in fact(5):
    print(x)

# print(*fact(5))
