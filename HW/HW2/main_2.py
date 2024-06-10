def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    print("{")
    for ingredient, values in shop_list.items():
        print(f"  '{ingredient}': {values},")
    print("}")

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  'Фахитос': [{'ingredient_name': 'Говядина', 'measure': 'г', 'quantity': 500},
                {'ingredient_name': 'Перец сладкий',
                 'measure': 'шт',
                 'quantity': 1},
                {'ingredient_name': 'Лаваш', 'measure': 'шт', 'quantity': 2},
                {'ingredient_name': 'Винный уксус',
                 'measure': 'ст.л',
                 'quantity': 1},
                {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': 2}]
}

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)