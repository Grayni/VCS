class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def destruct_str(cls, date):
        try:
            # По условию в задаче int уже валидируется интерпретатором Python в @classmethod
            # Проверять на int в @staticmethod смысла нет
            d, m, y = list(map(int, date.split('-')))
        except ValueError:
            return 'Строка должна содержать только цифры и -'
        else:
            return cls(d, m, y)

    def __str__(self):
        if self.validate(self.d, self.m, self.y):
            return f'day: {self.d}, month: {self.m}, year: {self.y}'
        else:
            return 'Исправьте ошибки'

    @staticmethod
    def validate(d, m, y):
        try:
            if not d in range(1, 32) or not m in range(1, 13) or y < 1000:
                raise SizeValueError('Число вне области значений')
            else:
                return 1
        except (SizeValueError, ValueError) as err:
            print(err)
            return 0


class SizeValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


date_1 = Date.destruct_str('31-12-2111')
print('date_1:', date_1)

date_2 = Date.destruct_str('11-11-d111')
print('date_2:', date_2)

date_3 = Date.destruct_str('1.1-11-1111')
print('date_3:', date_3)

date_4 = Date.destruct_str('11-15-1111')
print('date_4:', date_4)
