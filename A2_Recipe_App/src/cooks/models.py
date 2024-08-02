from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cook(models.Model):
    # username = models.OneToOneField(User, on_delete=models.CASCADE) - how to set default?
    name = models.CharField(max_length=50)
    fav_recipes = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
    )  # not sure if I used it right....

    def __str__(self):
        return str(self.name)
