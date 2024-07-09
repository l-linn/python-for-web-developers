recipes_list = []
ingredients_list = []

def take_recipe():
  name = input('Please give your recipe a name: ')
  cooking_time = input('How long is the cooking time? In minutes please: ')

  ingredients = [] #create an empty list then add user input into the list as list item
  print('Please list out the ingredients (type \'done\' when finished)') #skip quotes - adding backslash bedore hte single quotation 
  while True:
    ingredient = input('- ')
    if ingredient.lower() == 'done':
      break
    ingredients.append(ingredient)

  recipe = {
    'name': name,
    'cooking_time': cooking_time,
    'ingredients': ingredients
    }
  return recipe #need to return the variable to save it

n = int(input('How many recipes would you like to entre? '))

for i in range(n):
  recipe = take_recipe()

  for ingredient in recipe['ingredients']:
    if ingredient not in ingredients_list:
      ingredients_list.append(ingredient)
  
  recipes_list.append(recipe)


for recipe in recipes_list:
  cooking_time = int(recipe['cooking_time'])
  num_of_ingredients = len(recipe['ingredients'])
  difficulty = ''

  if cooking_time < 10 and num_of_ingredients < 4:
    difficulty = 'Easy'
  elif cooking_time < 10 and num_of_ingredients >= 4:
    difficulty = 'Medium'
  elif cooking_time >= 10 and num_of_ingredients >= 4:
    difficulty = 'Hard'
  else:
    print('Hmm, something is not right.')

  recipe['difficulty'] = difficulty #add difficulty as a key to the recipe dict

print('\nRecipes List:')
for recipe in recipes_list:
    print(f"Recipe Name: {recipe['name']}") #need to use double quotes for printing dict's key value pairs
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:\n- " + '\n- '.join(recipe['ingredients']))#use join method to join the values to one string, also can not use backslash in f string
    print(f"Difficulty Level: {recipe['difficulty']}")

sorted_ingredients_list = sorted(ingredients_list)

print('\nIngredients Available Across All Recipes\n- - - - - - - - - - - - - - - - - -')
for ingredient in sorted_ingredients_list:
  print(ingredient.capitalize())
