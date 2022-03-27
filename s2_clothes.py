from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        """ Function for calculation fabric consumption. """

    def __add__(self, other):
        summand_1 = self.fabric_consumption
        summand_2 = other.fabric_consumption
        return f'Sum fabric: {round(sum([summand_1, summand_2]), 2)}'


class Coat(Clothes):
    def __init__(self, v):
        self._V = v

    @property
    def fabric_consumption(self):
        return self._V/6.5 + 0.5

    def __str__(self):
        return f'Fabric consumption on coat: {round(self.fabric_consumption, 2)}'


class Suit(Clothes):
    def __init__(self, h):
        self._H = h

    @property
    def fabric_consumption(self):
        return 2 * self._H + 0.3

    def __str__(self):
        return f'Fabric consumption on suit: {round(self.fabric_consumption, 2)}'


coat = Coat(10)
suit = Suit(11)

print('Fabric for coat:', coat.fabric_consumption)
print('Fabric for suit:', suit.fabric_consumption)

print('')

print(coat)
print(suit)
print(coat + suit)


