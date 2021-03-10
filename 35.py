'''
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
'''

spec = '+'  # спецсимвол для завершения программы
flg = True  # флаг для проверки в цикле while
res_sum = 0  # итоговая сумма для вывода


def my_sum(a):
    sm = 0
    for el in a.split(' '):
        sm = sm + int(el)
    return sm


while flg:
    my_str = input('Введите строку чисел, разделённых пробелом: ')
    if my_str[-1] == spec:
        new_str = my_str[0:-2]
        res_sum = res_sum + my_sum(new_str)
        flg = False
        print(res_sum)
    else:
        res_sum = res_sum + my_sum(my_str)
        print(res_sum)
