from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.schemas.search_ingredient import SearchIngredient 
from db.session import get_db
from db.repository.search_ingredient import search_ingredient
from db.repository.recipes import create_new_recipe,recipe_delete
from db.repository.ingredients import create_new_ingredients
from db.repository.recipe_ingredient import couple_recipe_ingredient

router = APIRouter()

@router.get("/", response_model=SearchIngredient)
def search_ingredient(search:SearchIngredient, db:Session = Depends(get_db)):
    ingredients = search_ingredient(search, db)
    return ingredients

    
