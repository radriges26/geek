# Создать класс TrafficLight (светофор).


import time
import colorama
from colorama import Fore
colorama.init()


class TrafficLight:
    # приватный атрибут класса
    __color = "Красный"

    # метод класса
    def running(self):
        print(Fore.RED, end='')
        print(self.__color)
        time.sleep(7)  # пауза на 7 сек
        print(Fore.YELLOW, end='')
        self.__color = "Желтый"
        print(self.__color)
        time.sleep(2)  # пауза на 2 сек
        print(Fore.GREEN, end='')
        self.__color = "Зелёный"
        print(self.__color)
        time.sleep(4)  # пауза на 4 сек


a = TrafficLight()  # экземпляр класса
a.running()
