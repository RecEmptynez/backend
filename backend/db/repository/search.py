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
    print(recipe_list)
    total_ingredients = get_ingredients_from_recipe(recipe_list,db)

    return SearchResult(recipe_names = list(recipe_set))