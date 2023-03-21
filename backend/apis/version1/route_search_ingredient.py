from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.schemas.recipes import RecipeCreate,ShowRecipe,MultRecipesCreate,MultRecipesShow,DeleteRecipe,ShowDeletedRecipe
from db.schemas.search import Search 
from db.session import get_db
from db.repository.recipes import create_new_recipe,recipe_delete
from db.repository.ingredients import create_new_ingredients
from db.repository.recipe_ingredient import couple_recipe_ingredient
from db.repository.search import search_recipe
from typing import List
from db.schemas.search_ingredient import SearchIngredient, SearchIngredientResult
from db.repository.search_ingredient import search_ingredient

router = APIRouter()

@router.post("/ingredient")
def search_ingredients(search:SearchIngredient, db:Session=Depends(get_db)):
    ingredients = search_ingredient(search, db)
    return ingredients

