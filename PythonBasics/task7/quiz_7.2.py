"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    __totalCloth: float
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    @abstractmethod
    def countTotalCloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, v: int):
        super().__init__(name, v)
        self.countTotalCloth()

    @property
    def totalCloth(self):
        return self.__totalCloth

    def countTotalCloth(self):
        self.__totalCloth = self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, h: int):
        super().__init__(name, h)
        self.countTotalCloth()

    @property
    def totalCloth(self):
        return self.__totalCloth

    def countTotalCloth(self):
        self.__totalCloth = self.size*2 + 0.3


my_coat = Coat('spring', 180)
my_suit = Suit('work', 48)

print('Необходимое количество ткани: %0.2f' % (my_coat.totalCloth + my_suit.totalCloth))
