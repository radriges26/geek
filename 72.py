"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name_cloth, size):
        self.name_cloth = name_cloth
        self.size = size

    @abstractmethod
    def consumption_material(self):
        pass

    @property
    def my_method(self):
        return f"Переданные параметры:" \
            f" {self.name_cloth}, {self.size}"


class Coat(Clothes):
    def consumption_material(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def consumption_material(self):
        return self.size * 2 + 0.3


cl1 = Coat('Пальто', 32)
print(cl1.my_method)
print(f"Расход ткани = {cl1.consumption_material()}", end="\n\n")

cl2 = Suit('Костюм', 176)
print(cl2.my_method)
print(f"Расход ткани  = {cl2.consumption_material()}", end="\n\n")

print(f"Общий расход ткани = {cl1.consumption_material()+cl2.consumption_material()}")
