'''
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
'''

try:
    with open("text.txt", "a") as f_obj:
        while True:
            str_inp = input('Введите данные: ')
            if str_inp == '':
                break
            else:
                f_obj.write(str_inp+'\n')
except IOError:
    print("Произошла ошибка ввода-вывода!")