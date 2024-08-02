from django.test import TestCase
from .models import Recipe


# Create your tests here.
class RecipeTestCase(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="",
            cooking_time="",
            difficulty="",
            serves="",
            ingredients="",
            methods="",
        )

    def testRecipeName(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


# how do I test fav_recipes?
