# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

v = int(input('Выручка: '))
iz = int(input('Издержки: '))

if v > iz:
    print('Фирма отработала с прибылью')
    print('Рентабельность, в %:',(v - iz)/v*100)
    kol = int(input('Укажите кол-во сотрудников: '))
    print('Прибыль в расчете на одного сотрудника:', (v - iz) / kol)

else:
    print('Фирма отработала в убыток')