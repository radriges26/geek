"""
Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
"""
from abc import ABC, abstractmethod


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self):
        self.storage_list = []  # список склада, что есть
        self.storage_report_list = []  # отчет о перемещении оргтехники со склада в  опред. подразделение компании

    def get_office_equipment(self, equipment, count):
        equipment.to_take()['count'] = count
        self.storage_list.append(equipment.to_take())

    def give_office_equipment(self, equipment, count, department):
        if equipment.to_take()['count'] >= count:
            equipment.to_take()['count'] -= count
            tmp_dict = equipment.to_take().copy()
            tmp_dict['count'] = count
            tmp_dict['department'] = department
            self.storage_report_list.append(tmp_dict)
        else:
            print(f"\n На складе нет необходимого кол-ва. ({department} запрашивает {count}, а на складе всего {equipment.to_take()['count']})")


class OfficeEquipment(ABC):
    """класс родитель Оргтехника"""

    def __init__(self, name, model, dpi, speed):
        self.type = self.__class__.__name__
        self.name = name
        self.model = model
        self.dpi = dpi  # разрешение
        self.speed = speed  # скорость работы, листов в минуиту

    def group_name(self):
        return f'{self.type}'

    @abstractmethod
    def to_take(self):
        pass

    def __str__(self):
        return f"Оргтехника: {self.type}. Марка: {self.name},  модель: {self.model}"


class Printer(OfficeEquipment):
    """класс наследник Принтер"""

    def __init__(self, name, model, dpi, speed, chrominance):
        super().__init__(name, model, dpi, speed)
        self.chrominance = chrominance

    def to_take(self):
        return self.__dict__


class Scanner(OfficeEquipment):
    """класс наследник Сканер"""

    def __init__(self, name, model, dpi, speed, sensor):
        super().__init__(name, model, dpi, speed)
        self.sensor = sensor

    def to_take(self):
        return self.__dict__


class Xerox(OfficeEquipment):
    """класс наследник Ксерокс"""

    def __init__(self, name, model, dpi, speed, auto_feed=False):
        super().__init__(name, model, dpi, speed)
        self.auto_feed = auto_feed

    def to_take(self):
        return self.__dict__


p = Printer("HP", "M1132", 1200, 10, "цветной")
s = Scanner("CANON", "LiDE 300", 4800, 14, "CIS")
x = Xerox("Xerox", "B205", 2400, 30, True)

st = Storage()

p_count = input("Введите кол-во принтеров переданных на склад: ")
s_count = input("Введите кол-во сканеров переданных на склад: ")
x_count = input("Введите кол-во копиров переданных на склад: ")

try:
    if not p_count.isdigit() or not s_count.isdigit() or not x_count.isdigit():
        raise OwnError("Неверно указано кол-во. Исправьте, пожалуйста")
except OwnError as err:
    print(err)
else:

    st.get_office_equipment(p, int(p_count))
    st.get_office_equipment(s, int(s_count))
    st.get_office_equipment(x, int(x_count))

    print('-' * 130)

    # выводим состояние склада, вывожу посточно с номерами строк для наглядности
    for i, item in enumerate(st.storage_list):
        print(i, item)

    st.give_office_equipment(p, 3, "Бухгалтерия")  # забрали 1 принтер HP M1132 в отдел Бухгалтерии
    st.give_office_equipment(x, 2, "Отдел кадров")  # забрали 2 ксерокса Xerox B205 в отдел кадров

    print('-' * 130)

    # список куда и сколько переместили оргтехниики
    for i, item in enumerate(st.storage_report_list):
        print(i, item)

    print('-' * 130)

    # выводим состояние склада после перемещения
    for i, item in enumerate(st.storage_list):
        print(i, item)
