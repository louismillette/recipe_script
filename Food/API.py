'''
    File name: API.py
    Author: Louis Millette
    Date created: 11/07/2020
    Date last modified: 11/12/2020
    Python Version: 3.6
'''


import json
import os
import requests

class API():

	def _load_credentials(self):
		secret_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'secrets.txt')
		with open(secret_file, 'r') as file:
			self.apikey = file.readline().replace('\n', '')
		return self.apikey

	def call_recipes_api(self, ingredients, ignorePantry, number):
		apikey = self._load_credentials()
		results = requests.get(url = 'https://api.spoonacular.com/recipes/findByIngredients',
		             params = {
			             'ingredients': ingredients,
			             'ignorePantry': ignorePantry,
			             'number': number,
			             'apiKey': apikey,
		             })
		return results.json()

	def search_ingrediant(self, ingredient):
		apikey = self._load_credentials()
		results = requests.get(url = 'https://api.spoonacular.com/food/ingredients/search',
		             params = {
			             'query': ingredient,
			             'apiKey': apikey,
		             })
		return results.json()

	def get_recipe_price_breakdown(self, recipie_id):
		apikey = self._load_credentials()
		results = requests.get(f'https://api.spoonacular.com/recipes/{recipie_id}/priceBreakdownWidget.json?apiKey={apikey}')
		return results.json()
