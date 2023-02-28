from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate,DeleteRecipe,ShowDeletedRecipe
from db.models.recipes import Recipe
from db.models.recipe_ingredient import Recipe_ingredient
from db.models.ingredients import Ingredient
from sqlalchemy import Delete
from sqlalchemy import Select
from db.schemas.recipes import MultRecipesShow
import ingredients

def couple_recipe_ingredient(recipe_id:int, ingredient_id:int, importance:int, db:Session):
    db_recipe_ingredient = Recipe_ingredient(recipe_id=recipe_id, ingredient_id=ingredient_id, importance=importance)
    db.add(db_recipe_ingredient)
    db.commit()
    db.refresh(db_recipe_ingredient)
    return db_recipe_ingredient