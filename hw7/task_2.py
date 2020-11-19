# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
# ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    @abstractmethod
    def get_fabric_cost(self):
        pass


class Clothes(AbstractClothes):

    def __init__(self, fabric_cost=None):
        self.fabric_cost = fabric_cost

    def get_fabric_cost(self):
        return self.fabric_cost

    def __str__(self):
        return f'Fabric cost: {self.get_fabric_cost():.2f}'

    def __add__(self, other):
        return Clothes(self.get_fabric_cost() + other.get_fabric_cost())


class Coat(Clothes):

    def __init__(self, size):
        super().__init__()
        if not isinstance(size, int):
            raise ValueError(f'Invalid input size type: {type(size)}')
        else:
            self._size = size

    def get_fabric_cost(self):
        if self.fabric_cost is None:
            self.fabric_cost = self._size / 6.5 + 0.5
        return self.fabric_cost

    def __str__(self):
        return f'{super().__str__()} for coat'

    @property
    def size(self):
        return self._size


class Suit(Clothes):

    def __init__(self, height):
        super().__init__()
        try:
            self._height = float(height)
        except Exception:
            raise ValueError(f'Invalid input size type: {type(height)}')

    def get_fabric_cost(self):
        if self.fabric_cost is None:
            self.fabric_cost = self._height * 2 + 0.3
        return self.fabric_cost

    def __str__(self):
        return f'{super().__str__()} for suit'

    @property
    def height(self):
        return self._height


my_coat = Coat(42)
my_suit = Suit(1.73)
my_suit_for_work = Suit(1.73)

print(my_coat)
print(my_suit)

all_clothes = my_suit + my_coat + my_suit_for_work
print(all_clothes)
