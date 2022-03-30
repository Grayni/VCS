# A colony on Mars

class Humanity:
    ACCESS_LEVEL = 'D'

    def __init__(self, people=2, gender=None):
        self.people = people
        try:
            if not gender is None and gender['men'] + gender['women'] != self.people:
                raise PopulationError(f'Ошибка. Людей: {self.people}, {gender}. '
                                      'Расчет по среднему значению.')
            elif gender is None:
                self.gender = self.div_gen_half(self.people)
            else:
                self.gender = gender

        except PopulationError as err:
            print(err)
            self.gender = self.div_gen_half(self.people)

    @staticmethod
    def div_gen_half(people):
        men = round(people / 2)
        women = people - men
        return {'men': men, 'women': women}

    @staticmethod
    def show_population(population):
        return f'Население Марса: {population} марсиан(а)'

    def __add__(self, other):
        return Humanity(self.people + other.people)

    def __str__(self):
        return f'{self.people}'


class Engineers(Humanity):
    ACCESS_LEVEL = 'B'
    description = {}

    def __init__(self, profession, people, task='confidential'):
        super().__init__(people)
        self.__profession = profession
        self.task = task

    @property
    def profession(self):
        return self.__profession.upper()

    @staticmethod
    def ability(*args):
        print(f'Способности:')
        for i, ability in enumerate(args, 1):
            print(f'Cпособность_{i}: {ability}')


def description(profession, people, level, task):
    print(f'Профессия: {profession}')
    print(f'Количество человек: {people}')
    print(f'Уровень доступа: {level}')
    print(f'Задача: {task}')


class Building:
    LIST_PROFESSIONS = ['Агротехнолог', 'Инженер-робототехник', 'Инженер-геолог', 'Инженер-консруктор']

    def __init__(self, name, number_objects, professions, task):
        self.number_objects = number_objects
        self.name = name
        self.professions = professions
        self.task = task

    def description_building(self):
        print('Название объекта:', self.name)
        print('Количество необходимых объектов:', self.number_objects)
        print('Задействованные профессии:')
        for profession in self.professions:
            try:
                if profession in self.LIST_PROFESSIONS:
                    print('  -', profession)
                else:
                    raise ProfessionError('еще не прибыл')
            except ProfessionError as err:
                print('  -', profession, err)

        print('Функции строения:', self.task)


# Exceptions
class PopulationError(Exception):
    def __init__(self, txt):
        self.txt = txt


class ProfessionError(Exception):
    def __init__(self, txt):
        self.txt = txt


gp_astronauts_1 = Humanity()
gp_astronauts_2 = Humanity(10)
gp_astronauts_3 = Humanity(15)
gp_astronauts_4 = Humanity(35, {'men': 20, 'women': 15})

population = gp_astronauts_1 + gp_astronauts_2 + gp_astronauts_3 + gp_astronauts_4

print('~~ ЭКИПАЖИ И НАСЕЛЕНИЕ ~~', '\n')
print('Прибытие (1-4) экипажей:')
print(Humanity.show_population(population), end='\n\n')

print('Прибытие 5-ого экипажа:')
gp_astronauts_5 = Humanity(35, {'men': 40, 'women': 15})  # error men + women != people
print(f'Людей в 5 экипаже: {gp_astronauts_5} человека,', gp_astronauts_5.gender)
population += gp_astronauts_5
print(Humanity.show_population(population))
print(f'Класс доступа по умолчанию: {Humanity.ACCESS_LEVEL}', end='\n\n')

print('\n~~ ПРОФЕССИИ ~~\n')
robotics_engineer = Engineers('Инженер-робототехник', 17, 'Сборка системы андроидов для последующей автономности системы')
description(robotics_engineer.profession, robotics_engineer.people, robotics_engineer.ACCESS_LEVEL, robotics_engineer.task)
robotics_engineer.ability(
    'Обслуживание системных узлов',
    'Разработка компонентов для марсохода',
    'Корректировка автоматизированных процессов'
)
print('')
agrotechnologist = Engineers('Агротехнолог', 20, 'Возведение ферм и создание продуктов питания')
description(agrotechnologist.profession, agrotechnologist.people, agrotechnologist.ACCESS_LEVEL, agrotechnologist.task)
agrotechnologist.ability(
    'Селекция культур наиболее подходящих для жизни на Марсе',
    'Экспериментирование с местными породами и поиск полезных свойств для растений',
    'Поиск способов ускорения воспроизводства биопитания'
)

print('')
geologist_engineer = Engineers('Инженер-геолог', 15, 'Поиск места для строительства топливной станции')
description(geologist_engineer.profession, geologist_engineer.people, geologist_engineer.ACCESS_LEVEL, geologist_engineer.task)
geologist_engineer.ACCESS_LEVEL = 'C'
agrotechnologist.ability(
    'Поиск полезных ископаемых',
    'Отслеживание сейсмоактивности',
    'Поиск воды и новых видов почв'
)
print('')
design_engineer = Engineers('Инженер-конструктор', 45, 'Возведение базы обитания')
description(design_engineer.profession, design_engineer.people, design_engineer.ACCESS_LEVEL, design_engineer.task)
design_engineer.ACCESS_LEVEL = 'C'
design_engineer.ability(
    'Возведение необходимых строений',
    'Создание коммуникаций',
    'Возведение гермокупола'
)

print('\n\n~~ СТРОЕНИЯ ~~\n')
base = Building('"Цитадель"', 1, ['Инженер-консруктор', 'Инженер-робототехник', 'Инженер-геолог', 'Агротехнолог'], 'Главный пункт жизнедеятельности всех обитателей')
base.description_building()
print('')
farm = Building('Ферма', 20, ['Агротехнолог'], 'Объект с внутренней средой для разведения растительных культур')
farm.description_building()
print('')
fuel_station = Building('Топливная станция', 3, ['Инженер-консруктор', 'Инженер-геолог'], 'Добыча топлива и его хранение')
fuel_station.description_building()
print('')
laboratory = Building('Научная лаборатория', 2, ['Инженер-консруктор', 'Инженер-робототехник'], 'Разработка и сборка модулей')
laboratory.description_building()
print('')
warehouse = Building('Склад', 3, ['Кладовщик'], 'Хранение припасов и материалов')
warehouse.description_building()









