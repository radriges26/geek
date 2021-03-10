'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

even_list = [el for el in range(100, 1001) if el % 2 == 0]


def multiply(prev_el, el):
    return prev_el * el


print(reduce(multiply, even_list))

