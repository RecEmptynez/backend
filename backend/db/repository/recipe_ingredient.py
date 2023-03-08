from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate,DeleteRecipe,ShowDeletedRecipe
from db.models.recipes import Recipe
from db.models.recipe_ingredient import Recipe_ingredient
from db.models.ingredients import Ingredient
from sqlalchemy import Delete
from sqlalchemy import Select
from db.schemas.recipes import MultRecipesShow,ShowRecipe
from db.repository.ingredients import ingredient_in_database,get_ingredient_by_title

def couple_recipe_ingredient(recipe:ShowRecipe, importance:int, db:Session):
    ingredients = [get_ingredient_by_title(ingredient,db).id for ingredient in recipe.ingredients]
    for ingredient_id in ingredients:    
        db_recipe_ingredient = Recipe_ingredient(recipe_id=recipe.id, ingredient_id=ingredient_id, importance=importance)
        db.add(db_recipe_ingredient)
        db.commit()
        db.refresh(db_recipe_ingredient)
    return db_recipe_ingredient

def get_ingredients_from_recipe(recipes,db:Session) -> dict:
    recipe_ingredients = {}
    for recipe in recipes:
        stmt = Select(Recipe.id).where(Recipe.title==recipe)
        recipeid = db.execute(stmt).fetchall()[0][0]
        print(recipeid)
        stmt = Select(Recipe_ingredient.ingredient_id).where(Recipe_ingredient.recipe_id==recipeid)
        print(stmt)
        ingredient_ids = db.execute(stmt).fetchall()
        print(ingredient_ids)
    return recipe_ingredients