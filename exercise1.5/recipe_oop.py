class Recipe(object):
  def __init__(self, name, ingredients, cooking_time, difficulty):
    #class variable
    all_ingredients = set()
    ingredients = []

    self.name = name
    self.ingredients = ingredients
    self.cooking_time = int(cooking_time)
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
    cooking_time = cooking_time
  
  #method - add ingredients, packing arguments 
  def add_ingredients(self, *ingredients):
    for ingredient in ingredients:
      self.ingredients.append(ingredient)
    
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
  




