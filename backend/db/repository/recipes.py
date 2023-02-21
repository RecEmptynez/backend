from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate
from db.models.recipes import Recipe

#creates a new recipe and returns it
def create_new_recipe(recipe:RecipeCreate,db:Session):
    recipe = Recipe(
        title=recipe.title,
        url=recipe.url
    )
    db.add(recipe)
    db.commit() #commit gives the recipe an id
    db.refresh(recipe)
    return recipe

#creates a list of new recipes and returns them
def create_new_mult_recipes(recipes:MultRecipesCreate,db:Session):
    bulk_insert = [create_new_recipe(recipe=recipe,db=db) for recipe in recipes.recipes]
    return bulk_insert
        
