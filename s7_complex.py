class ComplexNumber:
    def __init__(self, complex_number):
        self.cn = complex_number

    def __str__(self):
        return f'{self.cn}'

    def __add__(self, other):
        return ComplexNumber(self.cn + other.cn)

    def __mul__(self, other):
        return ComplexNumber(self.cn * other.cn)


c1 = complex(-4, 3)
c2 = complex(3, 2)
print(f'Example: c1={str(c1).strip("()")}, c2={str(c2).strip("()")}')

z1 = ComplexNumber(c1)
z2 = ComplexNumber(c2)

print('Sum:', str(z1 + z2).strip('()'))  # -1+5j
print('Mul:', str(z1 * z2).strip('()'))  # -18+1j

