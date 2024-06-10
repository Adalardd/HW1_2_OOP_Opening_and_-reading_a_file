def read_recipe_file(file_name1, file_name2):
    cook_book = {}
    with open(file_name1, "r", encoding='utf-8') as orig, open(file_name2, "r+", encoding='utf-8') as d:
        for line in orig:
            if line.strip():
                d .write(line)
    with open(file_name2, "r", encoding='utf-8') as f:
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


cook_book = read_recipe_file("recipes.txt", "recipes1.txt")
print(cook_book)