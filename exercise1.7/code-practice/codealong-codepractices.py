# Connecting SQLAlchemy with Your Database
from sqlalchemy import create_engine

engine = create_engine("mysql://cf-python:password@localhost/my_database")

# Creating a Table from a Mapped Class
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy.types import Integer, String


# define class
class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"


# create tables
Base.metadata.create_all(engine)

# create a session on your database
from sqlalchemy.orm import sessionmaker

# nitialize the session object
Session = sessionmaker(bind=engine)
session = Session()

# Adding Entries to Your Table
tea = Recipe(name="Tea", cooking_time=5, ingredients="Tea Leaves, Water, Sugar")
# session.add(tea)
# comment it out to avoid adding it again

# -----------------------------------CODE PRACTICE 1-----------------------------------
coffee = Recipe(
    name="Coffee", cooking_time=5, ingredients="Coffee Powder, Sugar, Water"
)
# session.add(coffee)

cake = Recipe(
    name="Cake",
    cooking_time=50,
    ingredients="Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk",
)
# session.add(cake)

banana_smoothie = Recipe(
    name="Banana Smoothie",
    cooking_time=5,
    ingredients="Bananas, Milk, Peanut Butter, Sugar, Ice Cubes",
)
# session.add(banana_smoothie)


# Reading Entries from a Table
# all() method, which retrieves everything from the table as a list of objects:
recipes_list = session.query(Recipe).all()
for recipe in recipes_list:
    print("Recipe ID: ", recipe.id)
    print("Recipe Name: ", recipe.name)
    print("Ingredients: ", recipe.ingredients)
    print("Cooking Time: ", recipe.cooking_time)

# Retrieving a Single Object Using the get() Method
session.query(Recipe).get(1)

# -----------------------------------CODE PRACTICE 2-----------------------------------
# Using the filter() method to retrieve the recipes containing the ingredient sugar
recipe_has_sugar = (
    session.query(Recipe).filter(Recipe.ingredients.like("%Sugar%")).all()
)
print(recipe_has_sugar)

# deleteing recipes
# deleted_item = session.query(Recipe).filter(Recipe.name == "Banana Smoothie").first()
# session.delete(deleted_item)

# -----------------------------------CODE PRACTICE 3-----------------------------------
# accessing cake
print(recipes_list[2].ingredients)
recipes_list[2].ingredients += ", Chocolate powder"
print(recipes_list[2].ingredients)

# update one piece of content directly
session.query(Recipe).filter(Recipe.name == "Cake").update(
    {Recipe.name: "Birthday Cake"}
)
print(recipes_list[2].name)
# session.commit()  # use SELECT * FROM practice_recipes to check
