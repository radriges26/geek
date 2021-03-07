# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

lst = []

lst_count = int(input("Кол-во элементов списка : "))

for i in range(0, lst_count):
    el = int(input())
    lst.append(el)

if lst_count % 2 != 0:
    lst_count = lst_count -1

for i in range(0, lst_count, 2):
    lst[i],lst[i+1] = lst[i+1],lst[i]

print(lst)