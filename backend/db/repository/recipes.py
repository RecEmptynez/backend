from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate,DeleteRecipe
from db.models.recipes import Recipe

def create_new_recipe(recipe:RecipeCreate,db:Session):
    recipe = Recipe(
        title=recipe.title
    )
    db.add(recipe)
    db.commit() #commit gives the recipe an id
    db.refresh(recipe)
    return recipe

def create_new_mult_recipes(recipes:MultRecipesCreate,db:Session):
    bulk_insert = [create_new_recipe(recipe=recipe,db=db) for recipe in recipes.recipes]
    return bulk_insert

def delete_recipe(recipe:DeleteRecipe,db:Session):
    recipe = Recipe(
        id=recipe.id
    )
    deleted_recipe = db.delete()
    return deleted_recipe

