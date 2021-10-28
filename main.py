import os
from pprint import pprint
path = os.path.join(os.getcwd(), 'data.txt')
with open(path, encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp_data.append({'ingredient_name': ingredient_name.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()})
        cook_book[dish_name] = temp_data
        file.readline()
    pprint(cook_book)


    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for el_1 in dishes:
            for el_2 in cook_book[el_1]:
                if el_2['ingredient_name'] in shop_list.keys():
                    shop_list[el_2['ingredient_name']]['quantity'] += int(el_2['quantity']) * person_count
                else:
                    shop_list[el_2['ingredient_name']] = {}
                    shop_list[el_2['ingredient_name']]['measure'] = el_2['measure']
                    shop_list[el_2['ingredient_name']]['quantity'] = int(el_2['quantity']) * person_count
        print(shop_list)

    get_shop_list_by_dishes(['Омлет', 'Омлет'], 3)




