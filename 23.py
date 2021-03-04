# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = int(input())
my_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

if month > 12 or month < 1:
    print('Такого месяца не существует, время года определить невозможно ')
else:
    for key, value in my_dict.items():
        if month in value:
            print(key)