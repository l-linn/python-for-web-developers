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

  #Creating a new recipe
  def create_recipe(conn, cursor):
    return

  #Searching for a recipe by ingredient
  def search_recipe(conn, cursor):
    return

  #Updating an existing recipe
  def update_recipe(conn, cursor):
    return

  #Delete a recipe
  def delete_recipe(conn, cursor):
    return
  
  #loop running the main menu
  option=''
  while(option != 'exit'):
    print('================================================')
    print('Main Menu')
    print('================================================')
    print('What would you like to do? Please pick an option:')
    print('       1. Creating a new recipe\n       2. Searching for a recipe by ingredient\n       3. Updating an existing recipe\n       4. Deleting a recipe')
    print("\nOr type 'exit' to exit the programme")
    print('================================================')

    option = input('You choose to..(please input the index of the option)\n')
    
    if option == '1':
      create_recipe()
    elif option == '2':
      search_recipe()
    elif option == '3':
      update_recipe()
    elif option == '4':
      delete_recipe()
    else:
      print('Please pick an option number!')





  

main_menu(conn, cursor)


