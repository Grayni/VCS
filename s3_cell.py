class Cell:
    def __init__(self, num=0):
        self.num = num

    @staticmethod
    def check_func(part_1, part_2, operator):
        if isinstance(part_1, Cell) and isinstance(part_2, Cell):
            return Cell(round(eval(f'{part_1.num}{operator}{part_2.num}')))
        else:
            return 'Values should to belong by class "Cell"'

    @staticmethod
    def make_order(class_value, row_length):
        value = int(str(class_value))
        value_rows = value // row_length
        remains = value % row_length
        return ('*' * row_length + '\n') * value_rows + '*' * remains

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return self.check_func(self, other, '+')

    def __sub__(self, other):
        return self.check_func(self, other, '-')

    def __mul__(self, other):
        return self.check_func(self, other, '*')

    def __truediv__(self, other):
        return self.check_func(self, other, '/')


cell_1 = Cell(30)
cell_2 = Cell(10)
cell_3 = Cell(3)
number = 4

print('1.1) Sum of Cells:', cell_1 + cell_2 + cell_3)
print('1.2) Sum not of Cells:', cell_1 + number, '\n')

print('2.1) Sub of Cells:', cell_1 - cell_2 - cell_3)
print('2.2) Sub not of Cells:', cell_1 - number, '\n')

print('3.1) Mul of Cells:', cell_1 * cell_2 * cell_3)
print('3.2) Mul not of Cells:', cell_1 * number, '\n')

print('4.1) Div of Cells:', cell_1 / cell_2 / cell_3)
print('4.2) Div not of Cells:', cell_1 / number, '\n')


table_cells = Cell().make_order

print('instance: cell_1, cells: 30, number: 7')
print(table_cells(cell_1, 7), '\n')

print('instance: cell_2, cells: 10, number: 3')
print(table_cells(cell_2, 3), '\n')

print('instance: cell_3, cells: 3, number: 2')
print(table_cells(cell_3, 2), '\n')
