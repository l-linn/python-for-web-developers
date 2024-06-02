recipe_1 = {
  'name': 'Tea',
  'cooking_time_in_minutes' : 5,
  'ingredients':['Tea leaves','Suger','Water']
}

all_recipes = [recipe_1]

recipe_2 = { 
  'name': 'Banana Pancakes',
  'cooking_time_in_minutes' : 15,
  'ingredients':['Bananas','Eggs','Flour','Baking powder','Salt','Butter','Maple syrup','Fresh Berries']

}

recipe_3 = {
  'name': 'Tacos',
  'cooking_time_in_minutes' : 20,
  'ingredients':['Chicken','Taco seasoning','Taco shells','Lettuce','Tomatoes','Cheese','Sour cream','Salsa']
}

recipe_4 = {
  'name': 'Omelette',
  'cooking_time_in_minutes' : 10,
  'ingredients':['Eggs','Milk','Salt','Pepper','Cheese','Ham','Onions','Mushrooms']
}

recipe_5 = {
  'name': 'Chicken Stir-Fry',
  'cooking_time_in_minutes' : 25,
  'ingredients':['Chicken','Soy sauce','Hoisin sause','Sesame oil','Bell pepper','Broccoli','Garlic','Ginger','Rice']
}


all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

for i in all_recipes:
  i_ingredients = i.get('ingredients')
  print(i_ingredients)

