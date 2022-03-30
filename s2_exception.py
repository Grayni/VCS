class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        try:
            if self.b == 0:
                raise MyZeroDivisionError('В языке Python на ноль делить нельзя')
            else:
                return self.result(self.a/self.b)
        except MyZeroDivisionError as arr:
            return self.result(arr)

    @staticmethod
    def result(val):
        return f'Result: {val}'


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


ext_1 = Division(1, 2)
print(ext_1)

ext_2 = Division(1, 0)
print(ext_2)
