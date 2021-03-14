'''
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''
sum = 0
try:
    with open("only_nums.txt", "w+") as f_obj:
        str_inp = input('Введите числа через пробел: ')
        f_obj.write(str_inp)
        f_obj.seek(0)
        content = f_obj.read()
        for el in content.split():
            sum += int(el)
        print(sum)

except IOError:
    print("Произошла ошибка ввода-вывода!")