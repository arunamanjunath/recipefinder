import os
import json
from collections import namedtuple
import requests

api_key = os.environ.get("SPOONACULAR_API_KEY")
api_base_url = 'https://api.spoonacular.com/'
headers = {'Content-Type': 'application/json'}

class SpoonacularApi:
    def get_recipes(self, ingredients: str, number_of_recipes: int) -> list:
        """Takes a comma-separated list of ingredients and max number of recipes to fetch from spoonacular as input.
        Returns a list of spoonacular recipes."""
        resource_path = 'recipes/findByIngredients'
        payload = {'apiKey': api_key, 'ingredients': ingredients, 'number' : number_of_recipes, 'ignorePantry': 'false'}
        response = requests.get(api_base_url + resource_path, headers=headers, params=payload)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            raise Exception(f"Error retrieving recipes from Spoonacular. Http code - {response.status_code}")

    def get_ingredient_information(self, ingredient_id: int, amount: float, unit: str) -> dict:
        """Takes a spoonacular ingredient's id, ingredients amound (quantity), and measurement unit as input.
        Returns a dictionary with spoonacular ingredient information"""
        resource_path = 'food/ingredients/' + str(ingredient_id) + '/information'
        payload = {'apiKey': api_key, 'amount' : amount, 'unit': unit}
        response = requests.get(api_base_url + resource_path, headers=headers, params=payload)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            raise Exception(f"Error retrieving ingredient information from Spoonacular. Http code - {response.status_code}")
