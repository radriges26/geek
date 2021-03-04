# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
i = 0
new_el = int(input())

if new_el in my_list:
    my_list.insert(my_list.index(new_el), new_el)

else:
    for el in my_list:
        i += 1
        if el > new_el:
            continue
        else:
            my_list.insert(my_list.index(el), new_el)
            break

if i == len(my_list):
    my_list.append(new_el)

print(my_list)
