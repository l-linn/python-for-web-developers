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

    ## Convert Ingredients to a list - .splits()
    def format_ingredients_to_a_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")  # splits a string into a list.

    def calculate_difficulty(self):
        num_of_ingredients = len(self.format_ingredients_to_a_list())
        if self.cooking_time < 10 and num_of_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_of_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_of_ingredients <= 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_of_ingredients >= 4:
            self.difficulty = "Hard"
        else:
            print("Hmm, something is not right.")
