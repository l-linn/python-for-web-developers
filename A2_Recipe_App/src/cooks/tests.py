from django.test import TestCase
from .models import Cook
from recipes.models import Recipe


# Create your tests here.
class CookTestCase(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        # to write a test for a model that has a ForeignKey field,
        # you need to create an instance of the model that the ForeignKey points to
        # and then call save() on the ForeignKey instance,
        # before applying it to the creation of your target model for the test.

        fav_recipes = Recipe(name="Tacos")
        fav_recipes.save()
        Cook.objects.create(name="Craig", fav_recipes=fav_recipes)

    def testCookName(self):
        # Get a cook object to test
        cook = Cook.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its data
        field_label = cook._meta.get_field("name").verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, "name")

    def test_cook_name_max_length(self):
        # Get a cook object to test
        cook = Cook.objects.get(id=1)
        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = cook._meta.get_field("name").max_length
        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 50)


# how do I test fav_recipes?
