def read_recipes_from_file(file_name): recipes = []

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
                'name': ingredient[0],
                'quantity': ingredient[1],
                'unit': ingredient[2]
            })
        
        recipes.append({
            'name': recipe_name,
            'ingredients': ingredients
        })
        
        i += 2 + num_ingredients

    return recipes

def print_recipes(recipes):

    for recipe in recipes:

        print(recipe['name'])

        print("Ingredients:")

        for ingredient in recipe['ingredients']:

            print(f"{ingredient['name']} - {ingredient['quantity']} 

            {ingredient['unit']}")

        print()

file_name = 'recipes.txt'

recipes = read_recipes_from_file(file_name)

print_recipes(recipes)