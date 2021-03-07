'''
Нужно собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например, название.
Тогда значение — список значений-характеристик, например, список названий товаров.

'''

my_dict = {}  # получаемый словарь на выходе

n = int(input('Введите кол-во товаров: '))

prods = []  # список кортежей товаров

for i in range(1, n + 1):
    prod_name = input('Введите название товара: ')
    prod_price = int(input('Введите цену товара: '))
    prod_count = int(input('Введите кол-во товара: '))
    prod_unit = input('Введите ед.изм.: ')

    prods.append((i, {'название': prod_name, 'цена': prod_price, 'количество': prod_count, 'eд': prod_unit}))

list_name = []  # список названий товаров
list_price = []  # список цен товаров
list_count = []  # список кол-ва товаров
list_unit = []  # список ед. изм.

for el in prods:
    for el2 in el:
        if type(el2) == dict:
            for key, value in el2.items():

                if key == 'название':
                    list_name.append(value)
                    my_dict[key] = list_name

                if key == 'цена':
                    list_price.append(value)
                    my_dict[key] = list_price

                if key == 'количество':
                    list_count.append(value)
                    my_dict[key] = list_count

                if key == 'eд':
                    list_unit.append(value)
                    list_unit = list(set(list_unit))
                    my_dict[key] = list_unit

print(my_dict)
