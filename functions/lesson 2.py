def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    
    return shop_list

file_name = 'recipes.txt'
recipes = read_recipes_from_file(file_name)
cook_book = print_recipes(recipes)

dishes = ['Омлет', 'Запеченный картофель']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)