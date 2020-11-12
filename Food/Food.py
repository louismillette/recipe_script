from .API import API
from .AbstractFood import AbstractFood
import pprint

class Food(API, AbstractFood):

	def read_ingredients(self, ingrediant_list):
		ingredients = ingrediant_list.split(',')
		ingredients = [ele.strip() for ele in ingredients]
		for ingredient in ingredients:
			if self.search_ingrediant(ingredient)['totalResults'] == 0:
				ingredients.pop(ingredients.index(ingredient))
		return ingredients

	def search_recipes_online(self, ingredients, basic_pantry):
		ignorePantry = not basic_pantry
		recipes = self.call_recipes_api(ingredients, ignorePantry=ignorePantry, number=5)
		return recipes

	def add_prices_to_missed_ingredients(self, missed_ingredients, recipie_id):
		recipe_breakdown = self.get_recipe_price_breakdown(recipie_id)
		recipe_breakdown = {ele['name']:ele for ele in recipe_breakdown['ingredients']}
		i = 0
		while i < len(missed_ingredients):
			name = missed_ingredients[i].get('name')
			extended_name = missed_ingredients[i].get('extendedName') or name
			if not (recipe_breakdown.get(name) or recipe_breakdown.get(extended_name)):
				missed_ingredients[i]['price'] = 0
				missed_ingredients[i]['price_display'] = "$0"
			else:
				recipe_breakdown_match = recipe_breakdown.get(name) or recipe_breakdown.get(extended_name)
				missed_ingredients[i]['price'] = recipe_breakdown_match['price']
				missed_ingredients[i]['price_display'] = \
					f"${recipe_breakdown_match['price']}/{recipe_breakdown_match['amount']['us']['value']} {recipe_breakdown_match['amount']['us']['unit']}"
			i += 1
		return missed_ingredients

	def _basic_pantry(self):
		response = input("Before entering any ingrediants, would you like to include the pantry basics such as water, salt, flour, etc.? (y/n):")
		while 1:
			if not response in ['y', 'n']:
				response = input('Please enter "y" for yes or "n" for no: ')
				continue
			break
		return True if response == 'y' else False

	def _clean(self):
		pass

if __name__ == '__main__':
	f = Food()
	ingrediants = f.read_ingredients()
	recipes = f.search_recipes_online(ingrediants)
	shopping_list = f.show_recipes(recipes)
	f.display_shopping_list(shopping_list)
