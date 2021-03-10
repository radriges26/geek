'''
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
'''


def int_func(txt):
    return txt.capitalize()


latin_word = input('Введите слова через пробел маленькими латинскими буквами: ')

result = []
for word in latin_word.split(' '):
    result.append(int_func(word))

print(' '.join(result))