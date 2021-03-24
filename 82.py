# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

try:
    if int(num2) == 0:
        raise OwnError("Делитель = 0, а на 0 делить нельзя!")

except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления = {int(num1) / int(num2)}")
