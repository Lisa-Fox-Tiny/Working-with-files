import pprint
import os

with open ('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for recipes in file:
        cook_ingridient = int(file.readline())
        cook_list = []
        for i in range(cook_ingridient):
            ingridient_name, quantity, measure = file.readline().strip().split('|')
            cook_list.append({ 'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure })
        file.readline()

        cook_book[recipes.strip()] = cook_list
    pprint.pprint(cook_book)


def get_shop_list_by_dishes(dishes,person_count):
    dict_ = {}
    for dish, ingridients in cook_book.items():
        if dish in dishes:
            for i in ingridients:
                i['quantity'] = int(i['quantity']) * person_count
                dict_[i.get('ingridient_name')] = {'measure':i['measure'],'quantity':i['quantity']}
    print()
    pprint.pprint(dict_)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


def read_files(number):
    list_1 = []
    for i in range(1, number):
        name = f'sort\\{i}.txt'
        with open(name, 'r', encoding='utf-8') as f, open('sort\\newfile.txt', 'w', encoding='utf-8') as newfile:
            names = os.path.basename(name)
            res = f.readlines()
            len_str = len(res)
            str_text = ''.join(res)
            list_1.append((names, len_str, str_text.strip('\n')))
            list_res = list(sorted(list_1, key=lambda numb: numb[1]))
            for index in list_res:
                newfile.write(f'File name: {index[0]}\n')
                newfile.write(f'Number_lines: {index[1]}\n')
                newfile.write(f'{index[2]}\n')


read_files(4)
