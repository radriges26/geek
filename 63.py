# Реализовать класс Worker (работник)

class Worker:
    name = "Иван"
    surname = "Урюпин"
    position = "Специалист"
    _income = {"wage": 45000, "bonus": 27500}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"{self._income['wage'] + self._income['bonus']}")


a = Position()  # создаём экземпляр класса
print(a.position)  # получаем значение атрибута класса
a.get_full_name()  # метод получение имени и фамилии
a.get_total_income()  # метод выводит сумму доход+премия
