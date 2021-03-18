# Реализовать класс Stationery (канцелярская принадлежность)

class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


a = Stationery()
a.draw()

pn = Pen()
pn.draw()

psl = Pencil()
psl.draw()

hdl = Handle()
hdl.draw()
