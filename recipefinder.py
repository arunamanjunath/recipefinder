from abc import ABC, abstractmethod
import constant
import spoonacularclient
import time

class RecipeFinderInterface(ABC):
    @abstractmethod
    def parse_ingredients(self) -> dict:
        """Returns list of ingredients in the shopping list."""
        pass

    @abstractmethod
    def find_recipe(self, ingredients: str) -> str:
        """Given a comma-separated list of ingredients, returns a recipe with one or more of the specified ingredients."""
        pass
    
    @abstractmethod
    def get_shopping_list(self) -> dict:
        """Returns list of ingredients in the shopping list."""
        pass


#class SpoonacularRecipeFinder(RecipeFinderInterface):
class SpoonacularRecipeFinder:
    recipes = []
    shopping_list = []
    max_num_ingredients = constant.MAX_NUMBER_OF_INGREDIENTS
    max_num_recipes = constant.MAX_NUMBER_OF_RECIPES

    def find_recipe(self, ingredients: str) -> str:
        """Given a comma-separated list of ingredients, returns a recipe with one or more of the specified ingredients."""
        if len(ingredients.split(',')) > SpoonacularRecipeFinder.max_num_ingredients:
            raise ValueError('ERROR: Too many ingredients. Max number of ingredients allowed is 10.')
        
        SpoonacularRecipeFinder.recipes = spoonacularclient.get_recipes(ingredients, SpoonacularRecipeFinder.max_num_recipes)
        #SpoonacularRecipeFinder.recipes = [{'id': 524312, 'title': 'savory squash puree', 'image': 'https://spoonacular.com/recipeImages/524312-312x231.jpg', 'imageType': 'jpg', 'usedIngredientCount': 1, 'missedIngredientCount': 2, 'missedIngredients': [{'id': 11215, 'amount': 4.0, 'unit': 'cloves', 'unitLong': 'cloves', 'unitShort': 'cloves', 'aisle': 'Produce', 'name': 'garlic', 'original': '4 cloves garlic, minced', 'originalString': '4 cloves garlic, minced', 'originalName': 'garlic, minced', 'metaInformation': ['minced'], 'meta': ['minced'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/garlic.png'}, {'id': 11489, 'amount': 4.5, 'unit': 'pound', 'unitLong': 'pounds', 'unitShort': 'lb', 'aisle': 'Produce', 'name': 'hubbard squash', 'original': '1 4 ½ to 5 ½-pound Blue Hubbard Squash', 'originalString': '1 4 ½ to 5 ½-pound Blue Hubbard Squash', 'originalName': 'Blue Hubbard Squash', 'metaInformation': ['blue'], 'meta': ['blue'], 'extendedName': 'blue hubbard squash', 'image': 'https://spoonacular.com/cdn/ingredients_100x100/hubbard-squash.png'}], 'usedIngredients': [{'id': 5006, 'amount': 1.0, 'unit': 'cup', 'unitLong': 'cup', 'unitShort': 'cup', 'aisle': 'Meat', 'name': 'chicken', 'original': '1 cup reduced-sodium broth, vegetable or chicken, heated, divided', 'originalString': '1 cup reduced-sodium broth, vegetable or chicken, heated, divided', 'originalName': 'reduced-sodium broth, vegetable or chicken, heated, divided', 'metaInformation': ['divided', 'reduced-sodium'], 'meta': ['divided', 'reduced-sodium'], 'extendedName': 'low sodium chicken', 'image': 'https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg'}], 'unusedIngredients': [], 'likes': 46}, {'id': 1130755, 'title': 'Grilled Bone-In Chicken Thighs and Wingettes', 'image': 'https://spoonacular.com/recipeImages/1130755-312x231.jpg', 'imageType': 'jpg', 'usedIngredientCount': 1, 'missedIngredientCount': 2, 'missedIngredients': [{'id': 5091, 'amount': 10.0, 'unit': '', 'unitLong': '', 'unitShort': '', 'aisle': 'Meat', 'name': 'chicken thighs', 'original': '10 chicken thighs (about 5 lbs/2.25kgs), trim of excess fat', 'originalString': '10 chicken thighs (about 5 lbs/2.25kgs), trim of excess fat', 'originalName': 'chicken thighs (about 5 lbs/2.25kgs), trim of excess fat', 'metaInformation': ['( 5 lbs/2.25kgs)'], 'meta': ['( 5 lbs/2.25kgs)'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/chicken-thigh.jpg'}, {'id': 1012034, 'amount': 2.0, 'unit': 'tsp', 'unitLong': 'teaspoons', 'unitShort': 'tsp', 'aisle': 'Spices and Seasonings', 'name': 'Spice Rub', 'original': '2 tsp spice rub (any kind you prefer)', 'originalString': '2 tsp spice rub (any kind you prefer)', 'originalName': 'spice rub (any kind you prefer)', 'metaInformation': ['(any kind you prefer)'], 'meta': ['(any kind you prefer)'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/seasoning.png'}], 'usedIngredients': [{'id': 5006, 'amount': 0.5014814814814815, 'unit': 'g', 'unitLong': 'grams', 'unitShort': 'g', 'aisle': 'Meat', 'name': 'chicken', 'original': '10 to 11 chicken wingettes (about 1½/675g), trim off excess fat', 'originalString': '10 to 11 chicken wingettes (about 1½/675g), trim off excess fat', 'originalName': '10 to 11 chicken wingettes (about , trim off excess fat', 'metaInformation': [], 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg'}], 'unusedIngredients': [], 'likes': 1}]
        if len(SpoonacularRecipeFinder.recipes) == 0:
            print ("I have no recipes for your ingredients. Please try other imgredients.")
            return

        liked_a_recipe = False
        for recipe in SpoonacularRecipeFinder.recipes: 
            print("Here is a tasty recipe using your ingredients\n")
            print(f"\tName:  {recipe['title']}")

            print(f"\tYour ingredients used:")
            for user_ingredient in recipe["usedIngredients"]:
                print(f"\t\t\t{user_ingredient['name']}")

            if recipe["missedIngredientCount"] != 0:
                print(f"\tYou are missing {recipe['missedIngredientCount']} ingredients:")
                for missing_ingredient in recipe["missedIngredients"]:
                    print(f"\t\t\t{missing_ingredient['name']}")

            like = input("\nDo you like this recipe? \nType L if you do\nType any letter if you want a different one\n")
            if like == 'L':
                print ("\nHOORAY!! I will add the missing ingredients to your shopping list")
                for missing_ingredient in recipe["missedIngredients"]:
                    ingredient_info = spoonacularclient.get_ingredient_information(missing_ingredient['id'], missing_ingredient['amount'], missing_ingredient['unit'])
                    SpoonacularRecipeFinder.shopping_list.append(ingredient_info)
                liked_a_recipe = True
                break
            elif like != 'L':
                print ("No problem! I will try to find something better")
                continue

        if liked_a_recipe == False:
            print ("Sorry, I don't have any more recipes for your ingredients. Please try again with different ingredients.")
        
        print ("\nHold on please...Returning to main menu...")
        return 

    def get_shopping_list(self) -> dict:
        """Returns list of ingredients in the shopping list."""
        if len(SpoonacularRecipeFinder.shopping_list) == 0:
            print ("Your shopping list is empty")
            return

        total_cost = 0
        print ("Your shopping list:")
        for item in SpoonacularRecipeFinder.shopping_list:
            estimated_cost = item['estimatedCost']
            print (f"\tName: {item['name']}\tAisle: {item['aisle']}\tEstimated Cost: {estimated_cost}")
            total_cost += estimated_cost["value"]

        #assuming that all estimated costs returned by spoonacular are in USD and not cents
        print (f"Total estimated cost = {total_cost} us cents")
        print ("\nHold on please...Returning to main menu...")