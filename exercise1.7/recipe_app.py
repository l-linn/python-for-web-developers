from sqlalchemy import create_engine

# create a session on the database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# import modules
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy import CheckConstraint

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
				{"=" * 20}
				Recipe No.{self.id}
				Ingredients: {self.ingredients.title()}
				Cooking Time: {self.cooking_time} minutes
				Difficulty: {self.difficulty}
				{"=" * 20}"""

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


# Main Operations


## ------------------------------------FUNCTION 1 Create recipes--------------------------------------------
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
        # session.commit()

        print("> Recipe added!")
    # display a message after this function
    print("\n> All recipes added successfully!\nReturning to the main menu\n...\n..\n.")
    return


## ------------------------------------FUNCTION 2 VIEW ALL RECIPES------------------------------------------
def view_all_recipes():
    # get all recipes from the database.
    recipes = session.query(Recipe).all()
    # display a message if the recipe list is empty
    if not recipes:
        print()
        print("* " * 20)
        print("|" + " " * 10 + "NO SAVED RECIPES" + " " * 11 + "|")
        print("* " * 20)
        print("\n> Please add a recipe first!\n")
        return None

    # display header
    print()
    print("* " * 20)
    print("|" + " " * 10 + "VIEW ALL RECIPES" + " " * 11 + "|")
    print("* " * 20)

    # print all recipes
    for recipe in recipes:
        print(recipe.__str__)

    # print a total number of recipes
    total_recipe_number = len(recipes)
    print(
        f"\n> You have {total_recipe_number} recipes saved, well done!\nReturning to the main menu\n...\n..\n."
    )

    return


## ------------------------------------FUNCTION 3 SEARCH A RECIPE BY INGREDIENT-------------------------------
def search_recipe():
    # check if there is any recipes
    if session.query(Recipe).count() == 0:
        print()
        print("* " * 20)
        print("|" + " " * 10 + "NO SAVED RECIPES" + " " * 11 + "|")
        print("* " * 20)
        print("\n> Please add a recipe first!\nReturning to the main menu\n...\n..\n.")
        return

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
            """> What ingredients you want to include in your meal?
            Please choose a number from above
            Please separate multiple numbers with spaces:\n"""
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

    # a list contains like() conditions for every ingredient to be searched for
    conditions = []


# the main menu
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
        # elif option == "3":
        # update_recipe()
        # elif option == "4":
        # delete_recipe()
        elif option == "5":
            view_all_recipes()
        elif option == "exit":
            print("> Bye")
        else:
            print("> Please pick an option number!")
    session.close()
    engine.dispose()


main_menu()
