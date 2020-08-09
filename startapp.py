import os
import time
import sys
import recipefinder

def display_app_name():
    """Clears the terminal screen, and displays a title bar."""
    os.system('cls' if os.name == 'nt' else 'clear')
              
    print("***********************************")
    print("****  Aruna's Recipe Finder!  ****")
    print("***********************************")
    print("\nWelcome!! Want to find tasty, tasty recipes?")
    print("Tell me what ingredients you have at home. I will hook you up with an awesome recipe!\n")
    #print("\nType 'Q' to quit the app anytime.\n")
            

userinput = ''
ingredients = []
recipe_finder = recipefinder.SpoonacularRecipeFinder()
while userinput != 'S': 
    try:   
        display_app_name()
        
        print("What do you want me to do?")
        print("* Press 1 to Find a Recipe")
        print("* Press 2 to Show Shopping List")
        print("* Press S to Stop me")
        
        userinput = input("\nTake your pick: ")
        
        # Respond to the user's choice.
        if userinput == '1':
            print("\nLet's find you something yummy")
            useringredients = input("\nWhat ingredients do you have at home? (Enter a comma-separated list):\n")
            recipe_finder.find_recipe(useringredients)
            time.sleep(5)
        elif userinput == '2':
            recipe_finder.get_shopping_list()
            time.sleep(5)
        elif userinput == 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nEnjoy your meal. Bye!!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(r"Sorry, I'm programmed to do only 2 things ¯\_('')_/¯ ")
            print(r"Let's try again")
            time.sleep(5)
    except ValueError as error:
        print(error)
        print(r"Let's try again")
        time.sleep(5)
    except:
        print("Oops! I hit some unexpected issue. Please start me again.\n", sys.exc_info()[0])
        raise


