# Создать класс TrafficLight (светофор).


import time


class TrafficLight:
    # приватный атрибут класса
    __color = "Красный"

    # метод класса
    def running(self):
        print(self.__color)
        time.sleep(7)  # пауза на 7 сек
        self.__color = "Желтый"
        print(self.__color)
        time.sleep(2)  # пауза на 2 сек
        self.__color = "Зелёный"
        print(self.__color)
        time.sleep(4)  # пауза на 4 сек


a = TrafficLight()  # экземпляр класса
a.running()
