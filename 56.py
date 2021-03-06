'''
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
'''
import re

my_dict = {}

try:
    with open("school.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            hours_sum = 0  # кол-во занятий по каждому предмету
            hours = line.split(':')[1][1:-1]
            s1 = re.sub("[^0-9]", " ", hours)  # всё кроме цифр заменяем на пробелы
            for el in s1.split():
                hours_sum += int(el)
            my_dict[line.split(':')[0]] = hours_sum
        print(my_dict)

except IOError:
    print("Произошла ошибка ввода-вывода!")
