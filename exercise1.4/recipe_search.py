import pickle

#function to display all attributes of one recipe
def display_recipe(recipe):
  print(f"Recipe Name: {recipe['name']}") #need to use double quotes for printing dict's key value pairs
  print(f"Cooking Time (min): {recipe['cooking_time']}")
  print("Ingredients:\n- " + '\n- '.join(recipe['ingredients']))#use join method to join the values to one string, also can not use backslash in f string
  print(f"Difficulty Level: {recipe['difficulty']}")
   
def search_ingredient(data):
  sorted_all_ingredients = sorted(data['all_ingredients'])
  for ingredient in sorted_all_ingredients:
    ingredient.capitalize()

  print('\nIngredients Available Across All Recipes\n- - - - - - - - - - - - - - - - - -')
  #using enumerate in a for loop, takes in count and iterable
  for count, item in enumerate(sorted_all_ingredients, 1):
    print(count, item)
  
  try:
    choosed_number = int(input('Please choose a number that represents the ingredient you wish to include in your meal: '))
    ingredient_searched = sorted_all_ingredients[choosed_number - 1]
  except ValueError:
    print("Invalid input! Please enter a number.")
  except:
    print(f'Please enter a number between 1 and {len(sorted_all_ingredients) - 1}.')
  else:
    #using List Comprehension
    recipes_with_ingredient_searched = [recipe for recipe in data['recipe_list'] if ingredient_searched in recipe['ingredients']]
    for recipe in recipes_with_ingredient_searched:
      display_recipe(recipe)

#open user's file
user_filename = input('Please entre the name of your recipe collection:')

#execute search_ingredient function
try:
  with open('user_filename','rb') as user_file:
    data = pickle.load(user_file)
except FileNotFoundError:
    print("Collection not found. Please check your collection name and try again.")
else:
  search_ingredient(data)