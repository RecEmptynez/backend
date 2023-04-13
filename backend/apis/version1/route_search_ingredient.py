from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import get_db
from db.schemas.search_ingredient import SearchIngredient
from db.repository.search_ingredient import search_ingredient

router = APIRouter()

@router.post("/ingredient")
def search_ingredients(search:SearchIngredient, db:Session=Depends(get_db)):
    ingredients = search_ingredient(search, db)
    return ingredients

