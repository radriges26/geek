'''
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
'''


def int_func(txt):
    return txt.capitalize()


latin_letters = input('Введите строку из маленьких латинских букв: ')

print(int_func(latin_letters))
