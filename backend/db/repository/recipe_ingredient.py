from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate,DeleteRecipe,ShowDeletedRecipe
from db.models.recipes import Recipe
from db.models.recipe_ingredient import Recipe_ingredient
from db.models.ingredients import Ingredient
from sqlalchemy import Delete
from sqlalchemy import Select, func
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

# Gets all the ingredients from a recipe
def get_num_ingredients(recipe,db:Session) -> dict:
    stmt = Select(func.count(Recipe_ingredient.ingredient_id)).select_from(Recipe_ingredient).where(Recipe_ingredient.recipe_id == recipe)
    result = db.execute(stmt).fetchall()
    return result[0][0]