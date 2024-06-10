import pprint

def read_recipe_file(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = f.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure.strip()
                })
            cook_book[dish_name] = ingredients
    return cook_book

cook_book = read_recipe_file('recipes.txt')
pprint.pprint(cook_book)