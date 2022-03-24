class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        for val in self.arr:
            print(*val)
        return ''

    def __add__(self, other):
        print(f'sum matrix:\n{self.arr}\n{other.arr}\nresult:')

        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                self.arr[i][j] = self.arr[i][j] + other.arr[i][j]

        return Matrix(self.arr)


arr_1 = [[31, 32], [37, 43], [51, 86]]
arr_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
arr_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
arr_4 = [[5, 7, 6, 2], [1, 3, 6, 2]]

matrix_1 = Matrix(arr_1)
matrix_2 = Matrix(arr_2)
matrix_3 = Matrix(arr_3)
matrix_4 = Matrix(arr_4)

print(matrix_3 + matrix_4)

print('__init__')
print(matrix_1.arr)
print(matrix_2.arr)
print(matrix_3.arr)
print(matrix_4.arr)

print('\n__str__')
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_4)

