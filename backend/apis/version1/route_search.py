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

router = APIRouter()

@router.post("/recipes")
def search_recipes(search:Search, db:Session=Depends(get_db)):
    recipes = search_recipe(search,db)
    return search