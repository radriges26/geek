'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
new_list = []
try:
    with open("nums.txt") as f_obj:
        for line in f_obj:
            if '1' in line:
                new_list.append('Один - 1\n')
            if '2' in line:
                new_list.append('Два - 2\n')
            if '3' in line:
                new_list.append('Три - 3\n')
            if '4' in line:
                new_list.append('Четыре - 4\n')

except IOError:
    print("Произошла ошибка ввода-вывода!")

out_f = open("nums_ru.txt", "w")
out_f.writelines(new_list)
out_f.close()