'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def my_div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Делить на нуль нельзя')


fst_num = int(input())
sec_num = int(input())

my_div(fst_num, sec_num)