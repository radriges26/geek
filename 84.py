# Начните работу над проектом «Склад оргтехники».

class Storage:
    pass


class OfficeEquipment:
    """класс родитель Оргтехника"""

    def __init__(self, type_equipment, name, model, dpi, speed):
        self.type_equipment = type_equipment
        self.name = name
        self.model = model
        self.dpi = dpi  # разрешение
        self.speed = speed  # скорость работы, листов в минуиту

    def __str__(self):
        return f"Тип оргтехники: {self.type_equipment}, марка: {self.name},  модель: {self.model}"


class Printer(OfficeEquipment):
    """класс наследник Принтер"""

    def __init__(self, type_equipment, name, model, dpi, speed, chrominance):
        super().__init__(type_equipment, name, model, dpi, speed)
        self.chrominance = chrominance


class Scanner(OfficeEquipment):
    """класс наследник Сканер"""

    def __init__(self, type_equipment, name, model, dpi, speed, sensor):
        super().__init__(type_equipment, name, model, dpi, speed)
        self.sensor = sensor


class Xerox(OfficeEquipment):
    """класс наследник Ксерокс"""

    def __init__(self, type_equipment, name, model, dpi, speed, auto_feed=False):
        super().__init__(type_equipment, name, model, dpi, speed)
        self.auto_feed = auto_feed


p = Printer("Принтер", "HP", "M1132", 1200, 10, "цветной")
print(p)

s = Scanner("Сканер", "CANON", "LiDE 300", 4800, 14, "CIS")
print(s)

x = Xerox("Ксерокс", "Xerox", "B205", 2400, 30, True)
print(x)
