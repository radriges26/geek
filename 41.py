'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''

# запуск скрипта с параметра из терминала
# python 41.py 44 200 1000

from sys import argv

script_name, output_hours, rate_hour, bonus = argv


def payment_calc():
    result = int(output_hours) * int(rate_hour) + int(bonus)
    return result


print(f"Зарплата = {payment_calc()} руб.")
