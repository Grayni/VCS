class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_v(self, h=5):
        """ Example: 20м * 5000м * 25(кг/м2*см) * 5см = 12500 т """
        print(f'Масса асфальта: {round((self._width * self._length * 25 * h) / 1000)} тонн')


length = int(input('Задайте длину полотна (м): '))
width = int(input('Задайте ширину полотна (м): '))
height = input('(опционально) Толщина полотна (см): ')

road = Road(length, width)

if height:
    height = int(height)
    road.calc_asphalt_v(height)
else:
    road.calc_asphalt_v()

