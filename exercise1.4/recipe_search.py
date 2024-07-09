
print('\nRecipes List:')
for recipe in recipes_list:
    print(f"Recipe Name: {recipe['name']}") #need to use double quotes for printing dict's key value pairs
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:\n- " + '\n- '.join(recipe['ingredients']))#use join method to join the values to one string, also can not use backslash in f string
    print(f"Difficulty Level: {recipe['difficulty']}")

sorted_all_ingredients = sorted(all_ingredients)

print('\nIngredients Available Across All Recipes\n- - - - - - - - - - - - - - - - - -')
for ingredient in sorted_all_ingredients:
  print(ingredient.capitalize())
