import os
from recipes import recipes
import json

class RecipesAdminForLink:
    def __init__(self):
        self.recipes_data = recipes.load_recipes()

    def get_recipes_by_ingredients(self, ingredient: str)->List[dict]:
        """
        Sort/filter a list of recipe entries to find recipes containing the ingredient.
        Parameters:
            ingredient: str - The ingredient to search for (e.g., "soy sauce")
            recipes: list[dict] - A list of recipe entries loaded from JSON
        """
        recipe_collection=[]
        with open('recipes/recipes.json', 'r') as file:
            recipes = json.load(file)
        for item in recipes:
            # Check each ingredient in the recipe's ingredients list
            for recipe_ingredient in item.get('ingredients', []):
                if ingredient.lower() in recipe_ingredient.lower():
                    recipe_collection.append(item)
                    break  # Found a match, no need to check other ingredients
        return recipe_collection
    
    def get_recipes_by_name_of_the_dish(self,name:str)->List[dict]:
        """
        Sort/filter a list of recipe entries to find recipes by name of the dish.
        Parameters:
            name: str - The name of the dish to search for (e.g., "Pasta")
            recipes: list[dict] - A list of recipe entries loaded from JSON
        """
        recipe_collection=[]
        with open('recipes/recipes.json', 'r') as file:
            recipes = json.load(file)
        for item in recipes:
            # Check if the name matches the recipe's name
            if name.lower() in item.get('name', '').lower():
                recipe_collection.append(item)
        return recipe_collection
    def get_recipes_by_date(self,date:str)->List[dict]:
        """
        Sort/filter a list of recipe entries to find recipes by date.
        Parameters:
            date: str - The date to search for (e.g., "2023-10-01")
            recipes: list[dict] - A list of recipe entries loaded from JSON
        """
        recipe_collection=[]
        with open('recipes/recipes.json', 'r') as file:
            recipes = json.load(file)
        for item in recipes:
            # Check if the date matches the recipe's date
            if date == item.get('date', ''):
                recipe_collection.append(item)
        return recipe_collection