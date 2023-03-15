from sqlalchemy.orm import Session
from db.schemas.recipes import RecipeCreate,DeleteRecipe,ShowDeletedRecipe,ShowRecipe
from db.models.recipes import Recipe
from db.schemas.search import Search
from db.models.categories import Category
from db.models.ingredients import Ingredient
from db.models.recipe_ingredient import Recipe_ingredient
from sqlalchemy import Delete, Insert, Select, Join, distinct
from db.schemas.search import SearchResult
from db.repository.recipe_ingredient import get_ingredients_from_recipe


# Search for recipes based on ingredients
def search_recipe(search:Search,db:Session):
    recipes = []

    for ingredient in search.ingredient_names:
        stmt = Select(distinct(Recipe.title)).select_from(Recipe).join(Recipe_ingredient,Recipe.id == Recipe_ingredient.recipe_id).join(Ingredient,Ingredient.id == Recipe_ingredient.ingredient_id).where(Ingredient.title.like(f'%{ingredient}%'))
        result = db.execute(stmt).fetchall()
        for recipe in result:
            if len(recipe[0]) > 0:
                recipes.append(recipe[0])
    
    recipe_set = set(recipes) #remove duplicates
    recipe_list= list(recipe_set)

    user_ingredients = search.ingredient_names
    total_ingredients = get_ingredients_from_recipe(recipe_list,db)

    matches = get_match(user_ingredients, total_ingredients)
    sorted = sort_matches(matches)

    return SearchResult(recipe_names = sorted)

#Get the matches between the user ingredients and the recipes
def get_match(user_ingredients, total_ingredients) -> tuple:
    matches = {}
    for recipe in total_ingredients:
        match = 0
        recipe_ingredients = total_ingredients[recipe]
        for ingredient in user_ingredients:
            for ing in recipe_ingredients:
                if re.search(ingredient+'*', ing) and abs(len(ingredient)-len(ing)) < 3: #tomat ska matcha med tomater inte med tomatpuré
                    match += 1
        if match > 0:
            matches[recipe] = [match,len(recipe_ingredients),match/len(recipe_ingredients)]

    return matches

#Sort the matches and return them in an order ranging from best to worst match
def sort_matches(matches:dict) -> list:
    sorted_matches = sorted(matches.items(), key=lambda x: x[1][2], reverse=True)
    return {k: v for k, v in sorted_matches}