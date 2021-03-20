# Реализуйте класс Car

class Car:
    speed = 0
    color = "Черный"
    name = "Тесла"
    is_police = False

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")

    def show_speed(self, speed):
        self.speed = speed
        print(f"Скорость {self.name} = {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            print(f"Автомобиль {self.name} превысил скорость")
        else:
            print(f"Автомобиль {self.name} едет со скоростью = {self.speed}  км/ч")


class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40:
            print(f"Автомобиль {self.name} превысил скорость")
        else:
            print(f"Автомобиль {self.name} едет со скоростью = {self.speed}  км/ч")


class SportCar(Car):
    def get_info(self, name):
        self.name = name
        print(f"Автомобиль {self.name}, цвет {self.color}")


class PoliceCar(Car):
    def check(self, is_police):
        self.is_police = is_police
        if self.is_police:
            print("Авто полиции")
        else:
            print("Гражданский автомобиль")


a = Car()
a.go()
a.show_speed(49)
a.stop()
a.turn("налево")
print("-"*30)

b = TownCar()
b.show_speed(55)
a.turn("направо")
print("-"*30)

c = WorkCar()
c.go()
c.show_speed(47)
print("-"*30)

s = SportCar()
s.get_info("Audi R8")
s.show_speed(170)
print("-"*30)

p = PoliceCar()
p.stop()
p.check(False)
