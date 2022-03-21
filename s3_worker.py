class Worker:
    def __init__(self, income, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'\n{self.position}: {self.name} {self.surname}')

    def get_total_income(self):
        if not (self._income["wage"].isdigit() and self._income["bonus"].isdigit()):
            print('Оклад или премия не являются числами.')
            return

        print(f'Оклад + премия: {int(self._income["wage"]) + int(self._income["bonus"])} руб')


def func_data():
    d = input('Введите через пробел - Имя Фамилия Должность Оклад Премия: ')
    d = d.split()

    if len(d) != 5:
        print('\nОшибка ввода. Повторите попытку.\n')
        func_data()

    return d


data = func_data()

pos = Position({'wage': data[-2], 'bonus': data[-1]}, *data[:3])

pos.get_full_name()
pos.get_total_income()
