from functools import reduce

lst = [n for n in range(100, 1001) if not n % 2]

print(reduce(lambda x, y: x * y, lst))
