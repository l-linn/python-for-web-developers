from django.db import models


# Create your models here.
class Cook(models.Model):
    name = models.CharField(max_length=50)
    fav_recipes = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
    )  # not sure if I used it right....

    def __str__(self):
        return str(self.name)
