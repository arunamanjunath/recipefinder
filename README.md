App Name: Aruna’s Recipe Finder

Technology:
- Python 3.8.5

Required Libraries:
- requests Release v2.24.0 (Http library - https://requests.readthedocs.io/en/master/)

Steps:
1. Install Python 3.8.5
2. Install requests library
3. Set your Spoonacular API key in the system environment variable named "SPOONACULAR_API_KEY". The application reads the api key from the environment variable.
4. Open the directory where you cloned the "recipefinder" repo. Open the "dist" folder in the repo.
5. Run "startapp.exe" in the dist folder
    - The application is a console app and opens in a terminal
    - Read and follow the instructions on the terminal to use the app to find tasty, tasty recipes

Note: If you prefer to run the python script directly instead of the exe, follow steps 1 through 4 listed above and then 
    - open a terminal
    - cd into the directory where you cloned the "recipefinder" repo
    - Run command "python startapp.py" to start the application.


What does the app do?
1.	Given a list of ingredients, finds a tasty recipe from Spoonacular, an online collection of recipes
    - The recipes will include one or more of the ingredients you list
2.	For any recipe you like, Recipe Finder adds the ingredients you are missing for the recipe into a shopping list
    - If you do not like a recipe, the app simply searches for another great recipe!
3.	For your convenience, the shopping list will include, for each ingredient, the aisle in which you can find the ingredient in a grocery store as well as an estimated cost in US cents 
    - The shopping list will also give you the total estimated cost of all the missing ingredients in US cents.


Happy recipe search!!
