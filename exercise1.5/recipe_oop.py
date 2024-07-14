class Recipe(object):
  

  all_ingredients = set()
  def __init__(self, name):
    self.name = name
    self.ingredients = []
    self.cooking_time = int(0)
    #difficulty will be calculated later
    self.difficulty = None
  
  #methods - getter and setter for name and cooking_time
  def get_name(self):
    return self.name
  def set_name(self, name):
    self.name = name
  def get_cooking_time(self):
    return self.cooking_time
  def set_cooking_time(self, cooking_time):
    self.cooking_time = cooking_time
  
  #method - add ingredients, packing arguments 
  def add_ingredients(self, *ingredients):
    for ingredient in ingredients:
      self.ingredients.append(ingredient)
    #or use self.ingredients.extend(ingredients) to add multipul items?
    
    self.update_all_ingredients()
  
  #method - get the list of ingredients
  def get_ingredient_list(self):
    print('List of ingredients: ')
    print('\n- '.join(self.ingredients))
  
  #method - calculate difficulty
  def calculate_difficulty(self):
    num_of_ingredients = len(self.ingredients)
    if self.cooking_time < 10 and num_of_ingredients < 4:
      self.difficulty = 'Easy'
    elif self.cooking_time < 10 and num_of_ingredients >= 4:
      self.difficulty = 'Medium'
    elif self.cooking_time > 10 and num_of_ingredients < 4:
      self.difficulty = 'Intermediate'
    elif self.cooking_time > 10 and num_of_ingredients >= 4:
      self.difficulty = 'Hard'
    else:
      print('Something went wrong')
  
  #method - get difficulty or calculate difficulty if it hasn't been done
  def get_difficulty(self):
    if self.difficulty is None:
      self.calculate_difficulty()
    return self.difficulty
  
  #method - search for an ingredient, returns true or false
  def search_ingredient(self, ingredient):
    return ingredient in self.ingredients
  
  #method - goes through the current object’s ingredients and adds them to all_ingredients
  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      #add()method to add item to a set
      Recipe.all_ingredients.add(ingredient)

  #string representation
  def __str__(self):
    #use backslash to start a break a line
    output = 'Recipe Name: ' + self.name + \
    '\nCooking Time(in minutes): ' + str(self.cooking_time) + \
    '\nIngredients: ' + '\n- '.join(self.ingredients) + \
    '\nDifficulty: ' + self.get_difficulty() + \
    '\n---------------------'
    
    return output

#function to search a recipe by one ingredient
def recipe_search(data, search_term):
  #recipe parameter here is one of the objects that is created using class Recipe
  print('>>> Recipes that contain' + ' "' + search_term + '"' + ':\n---------------------')
  #not sure if it's better to use enumerate to label the recipes
  for count, recipe in enumerate(data, 1):
    if recipe.search_ingredient(search_term):
      print(count, recipe)

#create objects using Recipe class
tea = Recipe('Tea')
tea.add_ingredients('Tea Leaves','Sugar','Water')
tea.set_cooking_time(5)
#print(tea)

cake = Recipe('Cake')
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')
cake.set_cooking_time(50)

coffee = Recipe('Coffee')
coffee.add_ingredients('Coffee Powder', 'Sugar','Water')
coffee.set_cooking_time(5)

banana_smoothie = Recipe('Banana Smoothie')
banana_smoothie.add_ingredients('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes')
banana_smoothie.set_cooking_time(5)

recipes_list = [tea, cake, coffee, banana_smoothie]

recipe_search(recipes_list, 'Water')
recipe_search(recipes_list, 'Sugar')
recipe_search(recipes_list, 'Bananas')