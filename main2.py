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
