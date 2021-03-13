'''
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''

# используем файл text.txt из первого задания

try:
    with open("text.txt") as f_obj:
        for i, line in enumerate(f_obj,1):
            print(f"В {i} строке кол-во слов: {len(line.split())}, текст строки: {line}")
        print("-"*30)
        print(f"Кол-во строк в файле: {i}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
