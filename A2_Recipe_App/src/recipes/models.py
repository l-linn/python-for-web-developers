from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.CharField(
        max_length=20, help_text="Please input how long it takes in minutes"
    )
    # or models.IntegerField() instead?
    difficulty_choice = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("intermediate", "Intermediate"),
        ("hard", "Hard"),
    )
    difficulty = models.CharField(
        max_length=20, choices=difficulty_choice
    )  # String based on choice
    serves = models.CharField(max_length=20)
    ingredients = models.TextField()
    methods = models.TextField()

    def __str__(self):
        return str(self.name)
