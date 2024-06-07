recipes_list = []
ingredients_list = []

def take_recipe():
  name = input('Please give your recipe a name: ')
  cooking_time = input('How long is the cooking time? In minutes please: ')
  
  ingredients = []
  ingredients = input('Please list out the ingredients needed: ')

  recipe = {
    'name': name,
    'cooking_time': cooking_time,
    'ingredients': ingredients
    }
  
  print(recipe)
  return recipe

n = int(input('How many recipes would you like to entre? '))

for i in range(n):
  recipe = take_recipe()

