class Stationery:
    title = 'Запуск отрисовки'

    def draw(self):
        print(self.title)


class Pen(Stationery):
    def draw(self):
        print(f'Пишущий предмет - {self.title}. Она пишет хорошо.')


class Pencil(Stationery):
    def draw(self):
        print(f'Пишущий предмет - {self.title}. Им хорошо рисовать графику.')


class Handle(Stationery):
    def draw(self):
        print(f'Пишущий предмет - {self.title}. Идеальный инструмент для выделения главного.')


stat = Stationery()
stat.draw()

pen = Pen()
pen.title = 'Ручка'
pen.draw()

pencil = Pencil()
pencil.title = 'Карандаш'
pencil.draw()

handle = Handle()
handle.title = 'Маркер'
handle.draw()

