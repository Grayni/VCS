from itertools import cycle, count

lst = []

for num in count(3):
    lst.append(num)
    if num == 10:
        break

i = 69420
for num in cycle(lst):
    i -= 1
    print(num)
    if i == 0:
        break
