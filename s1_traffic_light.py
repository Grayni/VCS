import time
from itertools import cycle


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 4}

    def __init__(self, rep):
        self.rep = rep

    def running(self):
        for val in cycle(self.__color):
            if self.rep == 0 and val == 'Красный':
                print('Светофор на обслуживании...')
                break
            if val == 'Красный':
                self.rep -= 1

            print(val, end=' ')
            for y in range(self.__color[val], 0, -1):
                print(y, end=' ')
                time.sleep(1)
            print('')


repeat = int(input('Сколько раз повторить цветовой цикл? '))
tl = TrafficLight(repeat)

tl.running()
