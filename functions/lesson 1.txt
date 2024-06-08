# Функция read_recipes_from_file(file_name) открывает файл с именем file_name и считывает его содержимое.

# Данные обрабатываются в цикле, где каждая строка представляет собой новый рецепт.
 
# Для каждого рецепта извлекается его название, количество ингредиентов и список ингредиентов с их количеством и мерой.

# Все данные сохраняются в формате словаря и добавляются в список recipes. Функция возвращает список рецептов.



# Функция print_recipes(recipes) принимает список рецептов и конвертирует его в формат словаря, где ключами являются названия рецептов, а значениями - списки ингредиентов. 

#Далее возвращается конвертированный словарь cook_book.

#Код далее открывает файл 'recipes.txt', считывает рецепты, вызывает функции read_recipes_from_file(file_name) и print_recipes(recipes),

чтобы обработать данные и вывести их в формате словаря. Результат выводится на экран с помощью print.


def read_recipes_from_file(file_name):
    recipes = []
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        i = 0
        
        while i < len(lines):
            recipe_name = lines[i].strip()
            num_ingredients = int(lines[i+1])
            ingredients = []
            
            for j in range(i+2, i+2+num_ingredients):
                ingredient = lines[j].strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient[0],
                    'quantity': int(ingredient[1]),
                    'measure': ingredient[2]
                })
            
            recipes.append({
                'name': recipe_name,
                'ingredients': ingredients
            })
            
            i += 2 + num_ingredients
    
    return recipes

def print_recipes(recipes):
    cook_book = {}
    for recipe in recipes:
        ingredients_list = []
        for ingredient in recipe['ingredients']:
            ingredients_list.append({
                'ingredient_name': ingredient['name'],
                'quantity': int(ingredient['quantity']),
                'measure': ingredient['unit']
            })
        cook_book[recipe['name']] = ingredients_list
    
    return cook_book

file_name = 'recipes.txt'
recipes = read_recipes_from_file(file_name)
cook_book = print_recipes(recipes)
print(cook_book)