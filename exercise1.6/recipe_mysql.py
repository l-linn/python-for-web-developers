#Creating recipes and adding them to the database
#Searching for recipes on the database by ingredient
#Modifying entries in the database
#Deleting recipes from the database

import mysql.connector
#Create connector
conn = mysql.connector.connect(
  host='localhost',
  user='cf-python',
  passwd='password')
#initialize a cursor object
cursor = conn.cursor(buffered=True)
#create and use the database
cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')
cursor.execute('USE task_database')
#create recipe table
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients VARCHAR(225),
               cooking_time INT,
               difficulty VARCHAR (20))''')

#the main menu
def main_menu(conn, cursor):
  #loop running the main menu
  option=''
  while(option != 'exit'):
    print(f"{'=' * 13}")
    print('+ Main Menu +')
    print(f"{'=' * 13}")
    print('What would you like to do? Please pick an option:')
    print(f'''
          1. Creating a new recipe
          2. Searching for a recipe by ingredient
          3. Updating an existing recipe
          4. Deleting a recipe
          5. View all recipes''')
    print("\nOr type 'exit' to exit the programme")

    option = input('>>> You choose to..(please input the index of the option)\n').lower()
    
    if option == '1':
      create_recipe(conn, cursor)
    elif option == '2':
      search_recipe(conn, cursor)
    elif option == '3':
      update_recipe(conn, cursor)
    elif option == '4':
      delete_recipe(conn, cursor)
    elif option == '5':
      view_recipes(conn, cursor)
    elif option == 'exit' :
      print('Bye')
    else:
      print('Please pick an option number!')
  conn.close()

#Creating a new recipe
def create_recipe(conn, cursor):
  print('>>> Follow the steps to create a new recipe.')
  
  while True: #is the while loop necessary?
    try:
      number_of_recipes = int(input('How many recipes would you like to entre? '))
      if number_of_recipes < 1:
        print('Please entre a positive number.')
      else:
        break
    except ValueError:
        print('Please entre a number!')
    
  for i in range(number_of_recipes):
    print(f'=== Recipe NO.{i+1} ===')

    name = input('Please give your recipe a name: ')
    cooking_time = int(input('How long is the cooking time? In minutes please: '))

    ingredients = []
    print('Please list out the ingredients (type \'done\' when finished)') #skip quotes - adding backslash bedore hte single quotation 
      
    while True:
      ingredient = input('- ')
      if ingredient.lower() == 'done':
        break
      ingredients.append(ingredient)

    #MySQL doesn’t fully support arrays, your ingredients list needs to be converted into a comma-separated string.
    ingredients_str = ', '.join(ingredients)

    #call function to add difficulty to recipe
    difficulty = calculate_difficulty(int(cooking_time), len(ingredients))

    #wrap and insert the date above into MySQL
    insert_data_sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    user_input_value = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(insert_data_sql, user_input_value)

    #make the change
    conn.commit()

    print('Recipe added successfully!')
    print('\nReturn to Main Menu..')

#Calculare difficulty
def calculate_difficulty(cooking_time, num_of_ingredients):
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

#format and display the recipe
def display_recipe(row):
  print('Recipe NO.' + str(row[0]))
  print('   Recipe Name: ' + row[1])
  print('   Ingredients: ' + row[2])
  print('   Cooking Time: ' + str(row[3]))
  print('   Difficulty: ' + row[4] + '\n')

#Searching for a recipe by ingredient
def search_recipe(conn, cursor):
  #get a list of all ingredients that is available in the Recipes table
  cursor.execute("SELECT ingredients FROM Recipes")
  results = cursor.fetchall()# results here is a list of tuples
  #print(results)

  if not results:
    print('The ingredient list is empty..')

  all_ingredients = set()
  print('>>> Search a for a recipe that contains the ingrendient you like to have')

  #loop through results
  for result in results:
    print(result)
    ingredients_list = result[0].split(', ') #[0] returns the first element of a list.
    for ingredient in ingredients_list:
      ingredient.capitalize()
      all_ingredients.add(ingredient.strip())
      #print(all_ingredients)
  
  sorted_all_ingredients = sorted(all_ingredients)

  print('\nIngredients Available Across All Recipes\n- - - - - - - - - - - - - - - - - -')
  #using enumerate in a for loop, takes in count and iterable
  for count, item in enumerate(sorted_all_ingredients, 1):
    print(count, item.capitalize())

  try:
    choosed_number = int(input('Please choose a number that represents the ingredient you wish to include in your meal: '))
    ingredient_searched = sorted_all_ingredients[choosed_number - 1]
  except ValueError:
    print('Invalid input! Please enter a number.')
  except IndexError:
    print(f'Please enter a number between 1 and {len(sorted_all_ingredients) - 1}.')

  cursor.execute('SELECT * FROM Recipes WHERE ingredients LIKE %s',
                 ('%' + ingredient_searched + '%', ))
  
  recipes_with_ingredient_searched = cursor.fetchall()
  if recipes_with_ingredient_searched:
    for row in recipes_with_ingredient_searched:
      print('>>> Available Recipes:')
      display_recipe(row)
  else:
    print('Sorry, no recipe found.')

  print('Return to Main Menu..')

#Updating an existing recipe
def update_recipe(conn, cursor):
  cursor.execute('SELECT * FROM Recipes')
  results = cursor.fetchall()

  print('>>> Update an existing recipe')
  print('== List of all recipes ==')
  for row in results:
      display_recipe(row)
  
  choosen_recipe_id = int(input('Please entre the ID (No.) of recipe that you wish to update: '))
  cursor.execute('SELECT * FROM Recipes WHERE id = %s', (choosen_recipe_id))


  return

#Delete a recipe
def delete_recipe(conn, cursor):
  return
  
#view all recipes
def view_recipes(conn, cursor):
  return


main_menu(conn, cursor)


