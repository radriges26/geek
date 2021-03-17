'''
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить её в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.
'''
import json

my_list = []  # Итоговый список
comp_dict = {}  # словарь компаний и их прибыль
profit = 0
i = 0

try:
    with open("companies.txt") as f_obj:
        for line in f_obj:
            temp_list = line.rstrip().split(' ')
            comp_dict[temp_list[0]] = int(temp_list[2]) - int(temp_list[3])
            if (int(temp_list[2]) - int(temp_list[3])) > 0:
                i += 1
                profit += int(temp_list[2]) - int(temp_list[3])
        my_list.append(comp_dict)
        my_list.append({'average_profit': round(profit / i, 2)})
        print(my_list)

    with open("my_file.json", "w") as write_f:
        json.dump(my_list, write_f)

except IOError:
    print("Произошла ошибка ввода-вывода!")
