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
        # Get a cook object to test
        recipe = Recipe.objects.get(id=1)
        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field("name").max_length
        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 50)


# how do I test fav_recipes?
