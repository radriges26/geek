# Реализовать программу работы с органическими клетками, состоящими из ячеек.
class Cell:
    def __init__(self, cells):
        self.cells = cells

    def make_order(self, count):
        if self.cells < count:
            print("*" * count)
        else:
            for i in range(self.cells // count):
                print("*" * count)
            print("*" * (self.cells % count))

    def __str__(self):
        return f"Новая клетка, кол-во ячеек = {self.cells}"

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            return "Разность ячеек < 0"

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        try:
            return Cell(int(self.cells / other.cells))
        except ZeroDivisionError:
            return "Делить на 0 нельзя"


c1 = Cell(46)
c1.make_order(11)  # вывод с указанием кол-ва ячеек в ряду

c2 = Cell(4)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)  # деление с округлением до целого
