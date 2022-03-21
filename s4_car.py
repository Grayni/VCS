class Car:
    def __init__(self, speed=40, color='Black', name='TC', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Автомобиль начал движение')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, direction):
        print(f'Автомобиль повернул на{direction}')

    def show_speed(self):
        print(f'Скорость ТС составляет {self.speed} км/ч')

    def check_police(self):
        if self.is_police:
            print('This is a police transport')
        else:
            print('This is not a police transport')

    @staticmethod
    def limit_speed():
        print('Скорость превышена.')


class TownCar(Car):
    brand = 'Tesla'
    model = 'Model Plaid'
    autopilot = 'Artificial intelligence'
    class_car = 'Luxury'

    @classmethod
    def show_specifications(cls):
        print(f'Brand: {cls.brand}\nModel: {cls.model}\nAutopilot: {cls.autopilot}\nClass: {cls.class_car}')

    def show_basic(self):
        print(f'Type: {self.name}\nColor: {self.color}')

    def show_speed(self):
        if self.speed > 60:
            self.limit_speed()


class SportCar(Car):
    type_of_race = 'Formula-1'
    logo = 'Bull'
    rear_suspension = 'Carbon Fiber triangular rocker'

    def show_params(self):
        print(f'Type of race: {self.type_of_race}\nLogo: {self.logo}\n\
Rear suspension: {self.rear_suspension}\nColor:{self.color}')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            self.limit_speed()

    @staticmethod
    def data_output(type_car, purpose):
        print('\nAbout:')
        print(f'Type of vehicle: {type_car}\nPurpose: {purpose}')


class PoliceCar(Car):
    flashing_lights = False

    def switch_fl_lights(self):
        if self.flashing_lights:
            self.flashing_lights = False
            print('Проблесковый маячок включен')
        else:
            self.flashing_lights = True
            print('Проблесковый маячок выключен')


town_car = TownCar(100, 'Red', 'Electric Car', False)
print('\n-------------------------')
print(town_car.__class__.__name__, end='\n\n')
town_car.show_basic()
town_car.show_specifications()
town_car.check_police()
town_car.show_speed()
town_car.go()
town_car.turn('лево')
town_car.turn('право')
town_car.stop()


sport_car = SportCar(300, 'Blue', 'bolide', False)
print('\n-------------------------')
print(sport_car.__class__.__name__, end='\n\n')
sport_car.show_params()
sport_car.show_speed()
sport_car.go()
sport_car.turn('лево')
sport_car.stop()

work_car = WorkCar(80, 'Black', 'Special vehicle', False)
print('-------------------------')
print(work_car.__class__.__name__)
work_car.data_output('Dump truck', 'Sand')
print('Name:', work_car.name)
print('Color:', work_car.color)
print('')
work_car.go()
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(speed=1000)
print('-------------------------')
print(police_car.__class__.__name__, '\n')
police_car.check_police()
print('Color:', police_car.color)
police_car.show_speed()
print(police_car.is_police, end=' - ')
police_car.check_police()
police_car.is_police = True
print(police_car.is_police, end=' - ')
police_car.check_police()
police_car.switch_fl_lights()
police_car.switch_fl_lights()
police_car.go()
police_car.turn('лево')
police_car.turn('право')
police_car.turn('лево')
police_car.turn('право')
police_car.stop()