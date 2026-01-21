import recipe_admin_for_link

class MainApp:
    recipeAdmin=recipe_admin_for_link.RecipesAdminForLink()
    def run(self):
        # Example usage
        ingredient_search = "soy sauce"
        name_search = "Pasta"
        date_search = "2023-10-01"

        recipes_by_ingredient = self.recipeAdmin.get_recipes_by_ingredients(ingredient_search)
        recipes_by_name = self.recipeAdmin.get_recipes_by_name_of_the_dish(name_search)
        recipes_by_date = self.recipeAdmin.get_recipes_by_date(date_search)

        print(f"Recipes with ingredient '{ingredient_search}': {recipes_by_ingredient}")
        print(f"Recipes with name '{name_search}': {recipes_by_name}")
        print(f"Recipes with date '{date_search}': {recipes_by_date}")