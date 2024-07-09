import pickle

#Define empty lists
recipes_list = []
ingredients_list = []

#Define the function for calculating the recipe difficlty
def calc_difficulty(cooking_time, num_of_ingredients):
  difficulty=''
  if cooking_time < 10 and num_of_ingredients < 4:
    difficulty = 'Easy'
  elif cooking_time < 10 and num_of_ingredients >= 4:
    difficulty = 'Medium'
  elif cooking_time >= 10 and num_of_ingredients <= 4:
    difficulty = 'Intermediate'
  elif cooking_time >= 10 and num_of_ingredients >= 4:
    difficulty = 'Hard'
  else:
    print('Hmm, something is not right.')
  
  return difficulty

#Define the function for taking user input - recipe name, cooking time, ingredients
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

#call previous function to add difficulty to recipe
  difficulty = calc_difficulty(int(cooking_time), len(ingredients))

#put all attributes to a dictionary and return it
  recipe = {
  'name': name,
  'cooking_time': cooking_time,
  'ingredients': ingredients,
  'difficulty': difficulty
  }
  return recipe #need to return the variable to save it

#try-except-else-finally block to store and access user's data
user_filename = input('Please create a name for your recipe collection: ')

try:
  with open('user_filename','rb') as user_file:
    data = pickle.load(user_file)
except:
  






n = int(input('How many recipes would you like to entre? '))
for i in range(n):
  recipe = take_recipe()

  for ingredient in recipe['ingredients']:
    if ingredient not in ingredients_list:
      ingredients_list.append(ingredient)
  
  recipes_list.append(recipe)

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

