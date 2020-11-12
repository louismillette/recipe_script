'''
    File name: tests.py
    Author: Louis Millette
    Date created: 11/11/2020
    Date last modified: 11/12/2020
    Python Version: 3.6
'''

from Food.Food import Food
from Food.API import API

import unittest

class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.api = API()

    def test_load_credentials(self):
        credentials = self.api._load_credentials()
        self.assertIsInstance(credentials, str)

    def test_call_recipes_api(self):
        recipes = self.api.call_recipes_api("onions, green pepers, turmeric", False, 3)
        self.assertEqual(len(recipes), 3)
        names = [ele['title'] for ele in recipes]
        self.assertIn('Frying Pan Okra', names)
        self.assertIn("The Secret Ingredient (Turmeric): Maman's Yellow Peas and Onions", names)
        self.assertIn('Curried Onions', names)
        for recipe in recipes:
            self.assertEqual(list(recipe.keys()), ['id', 'title', 'image', 'imageType', 'usedIngredientCount', 'missedIngredientCount', 'missedIngredients', 'usedIngredients', 'unusedIngredients', 'likes'])

    def test_search_ingrediant(self):
        r1 = self.api.search_ingrediant('Frying Pan Okra')
        r2 = self.api.search_ingrediant('this is not an ingrediant')
        r3 = self.api.search_ingrediant(None)
        r4 = self.api.search_ingrediant(5)
        self.assertEqual(r1['number'], 10)
        self.assertEqual(r2['totalResults'], 0)
        self.assertEqual(r3['status'], 500)
        self.assertEqual(len(r4['results']), 2)

    def test_get_recipe_price_breakdown(self):
        r1 = self.api.get_recipe_price_breakdown(667373)
        self.assertIn('ingredients', r1.keys())
        self.assertIn('totalCost', r1.keys())
        self.assertIn('totalCostPerServing', r1.keys())
        r2 = self.api.get_recipe_price_breakdown(10511282)
        self.assertEqual(r2['code'], 404)

class FoodTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.food = Food()

    def test_read_ingredients(self):
        i1 = self.food.read_ingredients('onion, garlic')
        i2 = self.food.read_ingredients('onion, garlic, notingredient')
        i3 = self.food.read_ingredients(1)
        i4 = self.food.read_ingredients(None)

        self.assertEqual(i1, ['onion', 'garlic'])
        self.assertEqual(i2, ['onion', 'garlic'])
        self.assertEqual(i3, [])
        self.assertEqual(i4, [])

    def test_search_recipes_online(self):
        recipes1 = self.food.search_recipes_online(['onion', 'garlic', 'turmeric'], basic_pantry=True, number=3)
        self.assertEqual(len(recipes1), 3)
        for recipe in recipes1:
            self.assertEqual(list(recipe.keys()), ['id', 'title', 'image', 'imageType', 'usedIngredientCount', 'missedIngredientCount', 'missedIngredients', 'usedIngredients', 'unusedIngredients', 'likes'])

    def test_add_prices_to_missed_ingredients(self):
        missedIngredients =[
            {'id': 1001, 'amount': 1.0, 'unit': 'tablespoon', 'unitLong': 'tablespoon', 'unitShort': 'Tbsp',
             'aisle': 'Milk, Eggs, Other Dairy', 'name': 'butter', 'original': '1 tablespoon butter',
             'originalString': '1 tablespoon butter', 'originalName': 'butter', 'metaInformation': [], 'meta': [],
             'image': 'https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg'},
            {'id': 11278, 'amount': 1.0, 'unit': 'pound', 'unitLong': 'pound', 'unitShort': 'lb', 'aisle': 'Produce',
             'name': 'okra', 'original': '1 pound fresh okra, sliced in 1/8 inch pieces',
             'originalString': '1 pound fresh okra, sliced in 1/8 inch pieces',
             'originalName': 'fresh okra, sliced in 1/8 inch pieces',
             'metaInformation': ['fresh', 'sliced in 1/8 inch pieces'], 'meta': ['fresh', 'sliced in 1/8 inch pieces'],
             'extendedName': 'fresh okra', 'image': 'https://spoonacular.com/cdn/ingredients_100x100/okra.png'}]
        new_missed_ingredients = self.food.add_prices_to_missed_ingredients(missedIngredients, 667373)
        for new_missed_ingredient in new_missed_ingredients:
            self.assertIn('price', new_missed_ingredient.keys())
            self.assertIn('price_display', new_missed_ingredient.keys())

if __name__ == '__main__':
    unittest.main()
