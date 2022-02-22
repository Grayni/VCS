lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

lst = [num for num in lst if lst.count(num) == 1]

print(lst)
