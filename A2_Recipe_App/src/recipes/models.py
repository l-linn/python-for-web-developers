from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.CharField(max_length=20)
    # or models.IntegerField() instead?
    difficulty = models.CharField(max_length=20)
    serves = models.CharField(max_length=20)
    ingredients = models.TextField()
    methods = models.TextField()

    def __str__(self):
        return str(self.name)
