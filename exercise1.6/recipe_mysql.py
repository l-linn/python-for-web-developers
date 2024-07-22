import mysql.connector

# Create connector
conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")
# initialize a cursor object
cursor = conn.cursor(buffered=True)
# create and use the database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")
# create recipe table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes(
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients VARCHAR(225),
               cooking_time INT,
               difficulty VARCHAR (20))"""
)


# the main menu
def main_menu(conn, cursor):
    # loop running the main menu
    option = ""
    while option != "exit":
        print(f"{'=' * 13}")
        print("+ Main Menu +")
        print(f"{'=' * 13}")
        print("What would you like to do? Please pick an option:")
        print(
            f"""
          1. Create a new recipe
          2. Search for a recipe by ingredient
          3. Update an existing recipe
          4. Delete a recipe
          5. View all recipes"""
        )
        print("\nOr type 'exit' to exit the programme")

        option = input(
            ">>> You choose to..(please input the index of the option)\n"
        ).lower()

        if option == "1":
            create_recipe(conn, cursor)
        elif option == "2":
            search_recipe(conn, cursor)
        elif option == "3":
            update_recipe(conn, cursor)
        elif option == "4":
            delete_recipe(conn, cursor)
        elif option == "5":
            view_recipes(conn, cursor)
        elif option == "exit":
            print("Bye")
        else:
            print("Please pick an option number!")
    conn.close()


# Calculare difficulty
def calculate_difficulty(cooking_time, num_of_ingredients):
    difficulty = ""
    if cooking_time < 10 and num_of_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_of_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_of_ingredients <= 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and num_of_ingredients >= 4:
        difficulty = "Hard"
    else:
        print("Hmm, something is not right.")
    return difficulty


# update difficulty
def update_difficulty(new_difficulty, difficulty, recipe_id):
    if new_difficulty != difficulty:
        cursor.execute(
            "UPDATE Recipes SET difficulty = %s WHERE id = %s",
            (new_difficulty, recipe_id),
        )
        print(f"Recipe difficulty changed to: {new_difficulty}.")
    else:
        print("Recipe difficulty remains the same!")


# format and display the recipe
def display_recipe(row):
    print("Recipe No." + str(row[0]))
    print("   Recipe Name: " + row[1])
    print("   Ingredients: " + row[2])
    print("   Cooking Time: " + str(row[3]))
    print("   Difficulty: " + row[4] + "\n")


# Creating a new recipe
def create_recipe(conn, cursor):
    print(">>> Follow the steps to create a new recipe.")

    while True:  # is the while loop necessary?
        try:
            number_of_recipes = int(input("How many recipes would you like to entre? "))
            if number_of_recipes < 1:
                print("Please entre a positive number.")
            else:
                break
        except ValueError:
            print("Please entre a number!")

    for i in range(number_of_recipes):
        print(f"=== Recipe NO.{i+1} ===")

        name = input("Please give your recipe a name: ")
        cooking_time = int(input("How long is the cooking time? In minutes please: "))

        ingredients = []
        print(
            "Please list out the ingredients (type 'done' when finished)"
        )  # skip quotes - adding backslash bedore hte single quotation

        while True:
            ingredient = input("- ")
            if ingredient.lower() == "done":
                break
            ingredients.append(ingredient)

        # MySQL doesn’t fully support arrays, your ingredients list needs to be converted into a comma-separated string.
        ingredients_str = ", ".join(ingredients)

        # call function to add difficulty to recipe
        difficulty = calculate_difficulty(int(cooking_time), len(ingredients))

        # wrap and insert the date above into MySQL
        insert_data_sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
        user_input_value = (name, ingredients_str, cooking_time, difficulty)
        cursor.execute(insert_data_sql, user_input_value)

        # make the change
        conn.commit()

        print("Recipe added successfully!")
        print("\nReturn to Main Menu..")


# Searching for a recipe by ingredient
def search_recipe(conn, cursor):
    # get a list of all ingredients that is available in the Recipes table
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()  # results here is a list of tuples
    # print(results)

    if not results:
        print("The ingredient list is empty..")

    all_ingredients = set()
    print(">>> Search a for a recipe that contains the ingrendient you like to have")

    # loop through results
    for result in results:
        # print(result)
        ingredients_list = result[0].split(
            ", "
        )  # [0] returns the first element of a list.
        for ingredient in ingredients_list:
            ingredient.capitalize()
            all_ingredients.add(ingredient.strip())
            # print(all_ingredients)

    sorted_all_ingredients = sorted(all_ingredients)

    print(
        "\nIngredients Available Across All Recipes\n- - - - - - - - - - - - - - - - - -"
    )
    # using enumerate in a for loop, takes in count and iterable
    for count, item in enumerate(sorted_all_ingredients, 1):
        print(count, item.capitalize())

    try:
        choosed_number = int(
            input(
                "Please choose a number that represents the ingredient you wish to include in your meal: "
            )
        )
        ingredient_searched = sorted_all_ingredients[choosed_number - 1]
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    except IndexError:
        print(f"Please enter a number between 1 and {len(sorted_all_ingredients) - 1}.")
        return

    cursor.execute(
        "SELECT * FROM Recipes WHERE ingredients LIKE %s",
        ("%" + ingredient_searched + "%",),
    )

    recipes_with_ingredient_searched = cursor.fetchall()
    print(">>> Available Recipes:")
    if recipes_with_ingredient_searched:
        for row in recipes_with_ingredient_searched:
            display_recipe(row)
    else:
        print("Sorry, no recipe found.")
        return

    print("Return to Main Menu..")


# Updating an existing recipe
def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    print(">>> Update an existing recipe")
    print("== List of all recipes ==")
    for row in results:
        display_recipe(row)

    recipe_id = int(
        input("Please entre the ID (No.) of recipe that you wish to update: ")
    )
    # need to check if the input id exists, how?
    cursor.execute(
        "SELECT * FROM Recipes WHERE id = %s", (recipe_id,)
    )  # this has to be a tuple, list or dict hense the comma
    selected_recipe = cursor.fetchall()
    # print(selected_recipe)

    if selected_recipe:
        print(
            f"You have selected Recipe No.{selected_recipe[0][0]} {selected_recipe[0][1]}"
        )
        print(
            f"What would you like to update?\nPlease choose from:\n1. Recipe Name\n2. Cooking Time\n3. Ingredients"
        )
        update_option = input("Please entre the option number: ")

    # update recipe name
    if update_option == "1":
        updated_name = input("Please entre the new name for your recipe: ")
        cursor.execute(
            "UPDATE Recipes SET name = %s WHERE id = %s", (updated_name, recipe_id)
        )
        print(f"Recipe Name updated successfully to {updated_name}")

    # update cooking time
    elif update_option == "2":
        updated_cooking_time = int(
            input("Please entre the new cooking time in minutes: ")
        )
        cursor.execute(
            "UPDATE Recipes SET cooking_time = %s WHERE id = %s",
            (updated_cooking_time, recipe_id),
        )
        print("New cooking time added!")

        new_difficulty = calculate_difficulty(
            updated_cooking_time, len(selected_recipe[0][2].split())
        )
        update_difficulty(new_difficulty, selected_recipe[0][4], recipe_id)

    # update ingredients
    elif update_option == "3":
        updated_ingredients = []
        print(
            "Please re-entre all ingredients for this recipe (type 'done' when finished)"
        )

        while True:
            ingredient = input("- ")
            if ingredient.lower() == "done":
                break
            updated_ingredients.append(ingredient)

        print(updated_ingredients)

        updated_ingredients_str = ", ".join(updated_ingredients)

        cursor.execute(
            "UPDATE Recipes SET ingredients = %s WHERE id = %s",
            (updated_ingredients_str, recipe_id),
        )
        print("Ingredients updated!")

        # update difficulty if changes
        new_difficulty = calculate_difficulty(
            selected_recipe[0][3], len(updated_ingredients_str)
        )
        update_difficulty(new_difficulty, selected_recipe[0][4], recipe_id)

    else:
        print("Recipe does not exist")
    conn.commit()

    print("Return to Main Menu..")


# Delete a recipe
def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    print(">>> Delete a recipe")
    print("== List of all recipes ==")
    for row in results:
        display_recipe(row)

    recipe_id = int(
        input("Please entre the ID (No.) of the recipe you wish to delete: ")
    )
    cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id,))

    print("Deleting below recipe:")
    recipe_to_delete = cursor.fetchall()
    for row in recipe_to_delete:
        display_recipe(row)

    confirmed = input('Proceed to deletion, press "Y". Otherwise press "N"\n')
    if confirmed == "Y":
        cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
        print("Recipe deleted successfully!")
        print("Back to Main Menu..")
    elif confirmed == "N":
        print("Back to Main Menu..")
        return
    else:
        print('Please choose between "Y" and  "N"')

    conn.commit()
    return


# view all recipes
def view_recipes(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if len(results) == 0:
        print("\nNo recipes. Back to main menu.\n")
    else:
        print("== List of all recipes ==")
        for row in results:
            display_recipe(row)

    print("Return to Main Menu..")
    return


# run the app
main_menu(conn, cursor)
