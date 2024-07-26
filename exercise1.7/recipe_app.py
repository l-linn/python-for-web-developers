from sqlalchemy import create_engine

# create a session on the database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# import modules
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

# create engine
engine = create_engine("mysql://cf-python:password@localhost/my_database")

# Store your declarative base class into a variable
Base = declarative_base()

# initialize the session object
Session = sessionmaker(bind=engine)
session = Session()


# define Recipe model
class Recipe(Base):
    __tablename__ = "final_recipes"  # define table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  # nullable=False - can't leave it empty
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20))

    # quick representation of the recipe
    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"

    # detailed representation prints a well-formatted version of the recipe
    def __str__(self):
        return f"""
        Recipe ID: {self.id}
        Recipe Name: {self.name}
        Ingredients: {self.ingredients.title()}
        Cooking Time: {self.cooking_time} minutes
        Difficulty: {self.difficulty}
        {"= " * 16}"""

    # convert Ingredients to a list - .splits()
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")  # splits a string into a list.

    # function to calculate difficulty
    def calculate_difficulty(self):
        num_of_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_of_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_of_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_of_ingredients <= 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_of_ingredients >= 4:
            self.difficulty = "Hard"
        else:
            print("> Hmm, something is not right.")


# create tables
Base.metadata.create_all(engine)


# ------------------------------------------------5 FUNCTIONS------------------------------------------------
## ------------------------------------FUNCTION 1 CREATE RECIPES---------------------------------------------
def create_recipe():
    # print header
    print()
    print("* " * 20)
    print("|" + " " * 9 + "CREATE NEW RECIPES" + " " * 10 + "|")
    print("* " * 20)
    print("\n> Please follow the steps below to add new recipes!\n")

    # ask user for the number of recipes they want to add
    while True:
        try:
            number_of_recipes = int(
                input("> How many recipes would you like to entre?\n")
            )
            if number_of_recipes < 1:
                print("> Please add at least one recipe.")
            else:
                break
        except ValueError:
            print("> Please entre a number!")
        except Exception:
            print("> Something went wrong...")

    # loop over all the recipes user wants to add
    for i in range(1, number_of_recipes + 1):
        print("= " * 7 + "Recipe NO." + str(i) + " =" * 7)

        # ask for recipe name and check if it's under 50 characters
        while True:
            name = input("> Please give your recipe a name (50 characters max): ")
            if len(name.strip()) > 50:
                print("> Please give a shorter name for your recipe.")
            else:
                break

        # ask for cooking time and check if it's a positive number
        # instead of int using a different way of checking - .isnumeric()
        while True:
            cooking_time = input("> How long is the cooking time? In minutes please: ")
            if cooking_time.isnumeric() is True and int(cooking_time) > 0:
                break
            print("> Please enter a valid number")

        # ask for ingredients and check if it's under 255 characters
        ingredients = []
        print("> Please list out the ingredients (type 'done' when finish)")

        while True:
            ingredient = input("- ")
            if ingredient.lower() == "done":
                break
            ingredients.append(ingredient)

        # convert the list to a comma-separated string.
        ingredients_str = ", ".join(ingredients).title()

        # create new data entry
        recipe_entry = Recipe(
            name=name, ingredients=ingredients_str, cooking_time=int(cooking_time)
        )

        # calculate difficulty
        recipe_entry.calculate_difficulty()

        # add data to table
        session.add(recipe_entry)
        # commit changes
        # do I need to sdo something to make sure the commit has no problem?
        session.commit()

        print("> Recipe added!")
    # display a message after this function
    print("\n> All recipes added successfully!\nReturning to the main menu\n...\n..\n.")
    return


## ------------------------------------FUNCTION 2 VIEW ALL RECIPES-------------------------------------------
def view_all_recipes():
    # get all recipes from the database.
    recipes = session.query(Recipe).all()
    # display a message if the recipe list is empty
    if not recipes:
        no_recipe()

    # display header
    print()
    print("* " * 20)
    print("|" + " " * 10 + "VIEW ALL RECIPES" + " " * 11 + "|")
    print("* " * 20)

    # print all recipes
    for recipe in recipes:
        print(recipe.__str__())

    # print a total number of recipes
    total_recipe_number = len(recipes)
    print(f"\n> You have {total_recipe_number} recipes saved, well done!")

    return_to_main_menu()


## ------------------------------------FUNCTION 3 SEARCH A RECIPE BY INGREDIENT------------------------------
def search_recipe():
    # check if there is any recipes
    if session.query(Recipe).count() == 0:
        no_recipe()

    # get all ingredients from all recipes in the database.
    results = session.query(Recipe.ingredients).all()

    # create a set to store all ingredients
    all_ingredients = set()
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            all_ingredients.add(ingredient.strip())

    sorted_all_ingredients = sorted(all_ingredients)
    # print(sorted_all_ingredients)

    # print header
    print()
    print("* " * 20)
    print("|" + " " * 10 + "SEARCH FOR RECIPES" + " " * 10 + "|")
    print("* " * 20)

    print("\n> Search a for a recipe that contains the ingredient you like to have\n")

    print("= " * 20)
    print(" Ingredients across all saved recipes ")
    print("= " * 20)
    # print out all ingredients
    for count, item in enumerate(sorted_all_ingredients, 1):
        print(count, item.capitalize())

    # create a list to store user's input, this should be a list of integer
    chosen_numbers_list_int = []

    try:
        # user input would be something like : 1 4 5 15 and this will be a string "1 4 5 15"
        # use slipt to separate that string to a list of string ["1","4","5","15"]
        chosen_numbers = input(
            "> What ingredients you want to include in your meal?\n> Please choose a number from above\n> Please separate multiple numbers with spaces:\n"
        ).split()

        for number in chosen_numbers:
            number = int(number)
            if number <= 0 or number > len(sorted_all_ingredients):
                print("> Please enter numbers within the list above")
            else:
                chosen_numbers_list_int.append(number)

    except ValueError:
        print("> Invalid input! Please enter a number.")
        return

    except Exception:
        print("> Something went wrong...")
        return

    # list of corresponding ingredients - strings
    search_ingredients = []

    # loop through user's chosen number and find the corresponding ingredient from all_ingredients list
    for number in chosen_numbers_list_int:  # example list [1,2,3,4]
        ingredient = sorted_all_ingredients[number - 1]
        search_ingredients.append(ingredient)

    search_ingredients_str = ", ".join(search_ingredients)
    # print(search_ingredients)

    # a list contains like() conditions for every ingredient to be searched for
    conditions = []
    # Append the search condition
    for ingredient in search_ingredients:
        conditions.append(Recipe.ingredients.like(f"%{ingredient}%"))

    # print(conditions) # this is not readable ex. [<sqlalchemy.sql.elements.BinaryExpression object at 0x1032574c0>]
    matched_recipes = session.query(Recipe).filter(*conditions).all()

    # print header
    print("= " * 20)
    print(f"Recipes contains ingredients: {search_ingredients_str}")
    print("= " * 20)

    if matched_recipes:
        for recipe in matched_recipes:
            print(recipe.__str__())
    else:
        print("> Sorry, no recipe found!")

    print("\nRecipe search over.")
    return_to_main_menu()


## ------------------------------------FUNCTION 4 UPDATE RECIPES---------------------------------------------
def update_recipe():
    recipes = session.query(Recipe).all()
    print(recipes)
    # check if there is any recipes
    if not recipes:
        no_recipe()

    # print header
    print()
    print("* " * 20)
    print("|" + " " * 12 + "EDIT RECIPES" + " " * 13 + "|")
    print("* " * 20)

    print("\n> Select a recipe from the list below to edit\n")

    print_short_recipe()

    chosen_id = input("\n> Please entre the recipe ID to update that recipe: \n")
    # How do I return to a certain step instead of all the way back to main menu?

    results_id = session.query(Recipe.id).all()
    if chosen_id not in str(results_id):
        print("> Please choose a number that's in the list!")
    elif chosen_id.isnumeric() is False or int(chosen_id) < 0:
        print("> Please entre a valid number!")

    # recipe_to_edit = session.query(Recipe).get(
    # int(chosen_id))
    # got a warning - The Query.get() method is considered legacy as of the 1.x
    # use Session.get()
    recipe_to_edit = session.get(Recipe, int(chosen_id))

    if recipe_to_edit:
        print(f"> You selected Recipe NO.{recipe_to_edit.id} - {recipe_to_edit.name}")
        print(recipe_to_edit)

        user_confirmation = input(
            "> Is this the recipe you wanted? Please entre Y to continue or N to return.\n"
        )

        if user_confirmation.lower() == "y":

            print(
                """> What would you like to update?
                Please choose from:
                1. Recipe Name
                2. Ingredients
                3. Cooking Time"""
            )
        elif user_confirmation.lower() == "n":
            return
        else:
            print("> Please select from the given options")

    else:
        print("> No such recipe saved..")
        return_to_main_menu()

    update_option = input("Please entre the option number: ")

    # update recipe name
    if update_option == "1":
        updated_name = input(
            "> Please entre the new name for your recipe (50 characters max): "
        ).strip
        if len(update_option) <= 50:
            recipe_to_edit.name = updated_name
        else:
            print("> Please entre a shorter name!")

        print(f"> Recipe Name updated successfully to {updated_name}")

    # update ingredients
    elif update_option == "2":
        updated_ingredients = []
        print(
            "> Please re-entre all ingredients for this recipe (type 'done' when finished)"
        )

        while True:
            ingredient = input("- ")
            if ingredient.lower() == "done":
                break
            updated_ingredients.append(ingredient)

        # print(updated_ingredients)

        updated_ingredients_str = ", ".join(updated_ingredients)

        recipe_to_edit.ingredients = updated_ingredients_str
        print("> Ingredients updated!")

        # update difficulty if changes
        new_difficulty = recipe_to_edit.calculate_difficulty()
        update_difficulty(new_difficulty, recipe_to_edit.difficulty)

    # update cooking time
    elif update_option == "3":
        updated_cooking_time = int(
            input("> Please entre the new cooking time in minutes: ")
        )
        recipe_to_edit.cooking_time = updated_cooking_time

        print("> New cooking time added!")

        new_difficulty = recipe_to_edit.calculate_difficulty()
        update_difficulty(new_difficulty, recipe_to_edit.difficulty)

    else:
        print("> Recipe does not exist")

    session.commit()

    return_to_main_menu()


## ------------------------------------FUNCTION 5 DELETE RECIPES---------------------------------------------
def delete_recipe():

    if session.query(Recipe).count() == 0:
        no_recipe()
    # print header
    print()
    print("* " * 20)
    print("|" + " " * 11 + "DELETE RECIPES" + " " * 12 + "|")
    print("* " * 20)

    print("\n> Select a recipe from the list below to delete\n")

    print_short_recipe()

    chosen_id = input("\n> Please entre the recipe ID to delete that recipe: \n")

    results_id = session.query(Recipe.id).all()

    if chosen_id not in str(results_id):
        print("> Please choose a number that's in the list!")
    elif chosen_id.isnumeric() is False or int(chosen_id) < 0:
        print("> Please entre a valid number!")

    recipe_to_delete = session.get(Recipe, int(chosen_id))

    if recipe_to_delete:
        user_confirmation = input(
            "> Is this the recipe you want to delete? Please entre Y to continue or N to return.\n"
        )

        if user_confirmation.lower() == "y":
            session.delete(recipe_to_delete)
            session.commit()
            print("> Recipe deleted successfully!")
        elif user_confirmation.lower() == "n":
            print("> Action cancelled.\n")
        else:
            print("> Please select from the given options")
    else:
        print("> no such recipe!")

    return_to_main_menu()


# ------------------------------------------------MAIN MENU--------------------------------------------------
def main_menu():
    # loop running the main menu
    option = ""
    while option != "exit":
        print()
        print("* " * 20)
        print("|" + " " * 14 + "Main Menu" + " " * 14 + "|")
        print("* " * 20)
        print("\n> What would you like to do?")
        print(
            """
          1. Create a new recipe
          2. Search for a recipe by ingredient
          3. Update an existing recipe
          4. Delete a recipe
          5. View all recipes"""
        )
        print("\n> Please pick an option")
        print("> Or type 'exit' to exit the programme")

        option = input("\n> You choose to..(please input an index)\n").lower()

        if option == "1":
            create_recipe()
        elif option == "2":
            search_recipe()
        elif option == "3":
            update_recipe()
        elif option == "4":
            delete_recipe()
        elif option == "5":
            view_all_recipes()
        elif option == "exit":
            print("> Bye")
        else:
            print("> Please pick an option number!")
    session.close()
    engine.dispose()


# --------------------------------------FUNCTION TO RETURN TO MAIN MENU--------------------------------------
def return_to_main_menu():
    print("\nReady to return to the main menu? Press ENTER")
    input()
    print("\nReturning to the main menu\n...\n..\n.")


# --------------------------------------FUNCTION TO UPDATE DIFFICULTY--------------------------------------
def update_difficulty(new_difficulty, difficulty):
    if new_difficulty != difficulty:
        new_difficulty = difficulty
        print(f"> Recipe difficulty changed to: {new_difficulty}.")
    else:
        print("> Recipe difficulty remains the same!")


# --------------------------------------FUNCTION TO RETURN NO RECIPE MESSAGE---------------------------------
def no_recipe():
    print()
    print("* " * 20)
    print("|" + " " * 10 + "NO SAVED RECIPES" + " " * 11 + "|")
    print("* " * 20)
    print("\n> Please add a recipe first!\n")
    return_to_main_menu()


# --------------------------------------FUNCTION TO PRINT SHORTEN RECIPES--------------------------------------
def print_short_recipe():
    print("* " * 20)
    print("|" + " " * 12 + "ALL RECIPES" + " " * 14 + "|")
    print("* " * 20)
    results = session.query(Recipe.id, Recipe.name).all()
    # print all recipes, but only display the name and id
    for result in results:
        result_id = result[0]
        result_name = result[1]
        print(f"Recipe NO.{result_id} - {result_name}")


main_menu()
