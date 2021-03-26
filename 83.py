# Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


minus = False
num_list = []  # список, который будет заполняться только числами

while True:
    el = input("Введите число: ")
    if el[0] == "-":
        minus = True
        el = el[1:]

    try:
        if not el.isdigit() and el != "stop":
            raise OwnError("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        if el == "stop":
            break

        if minus:
            el_list = int(el) * -1
            minus = False
        else:
            el_list = int(el)

        num_list.append(el_list)

        print(f"Все хорошо. Вводите дальше")

print(f"Полученный список: {num_list}")
