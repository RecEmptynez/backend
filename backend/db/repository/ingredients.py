from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate,DeleteRecipe,ShowDeletedRecipe
from db.models.recipes import Recipe
from db.models.recipe_ingredient import Recipe_ingredient
from db.models.ingredients import Ingredient
from sqlalchemy import Delete
from sqlalchemy import Select
from db.schemas.recipes import MultRecipesShow

#checks if the ingredient is already in the database, returns true if it is
def ingredient_in_database(ingredient_name:str,db:Session):
    get_stmt = Select(Ingredient).where(Ingredient.name == ingredient_name)
    result = db.execute(get_stmt).fetchall()
    return len(result) > 0