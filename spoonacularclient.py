import os
import json
from collections import namedtuple
import requests

api_key = os.environ.get("SPOONACULAR_API_KEY")
api_base_url = 'https://api.spoonacular.com/'
headers = {'Content-Type': 'application/json'}

def get_recipes(ingredients: str, number_of_recipes: int):
    resource_path = 'recipes/findByIngredients'
    payload = {'apiKey': api_key, 'ingredients': ingredients, 'number' : number_of_recipes, 'ignorePantry': 'false'}
    response = requests.get(api_base_url + resource_path, headers=headers, params=payload)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_ingredient_information(ingredient_id: int, amount: float, unit: str):
    resource_path = 'food/ingredients/' + str(ingredient_id) + '/information'
    payload = {'apiKey': api_key, 'amount' : amount, 'unit': unit}
    response = requests.get(api_base_url + resource_path, headers=headers, params=payload)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
